import flet as ft
import json
import os
import asyncio
import sys
import SeerGPT.cards as cards

debug_flag = True if os.getenv("DEBUG") == "1" else False

def validate_config():
    config_path = cards.resource_path("config.json")
    try:
        if not os.path.exists(config_path):
            return False
        with open(config_path, "r") as f:
            content = f.read().strip()
            if not content:
                return False
            config = json.loads(content)
        required_keys = ["provider", "api_key", "non_reasoning_model", "reasoning_model"]
        for key in required_keys:
            if key not in config or not config[key]:
                return False
        return True
    except Exception as e:
        print("Error reading config.json:", e)
        return False

def show_setup_screen(page: ft.Page):
    async def on_setup_submit(e):
        config = {
            "provider": provider_dropdown.value,
            "api_key": api_key_field.value.strip(),
            "non_reasoning_model": non_reasoning_field.value.strip(),
            "reasoning_model": reasoning_field.value.strip()
        }
        with open(cards.resource_path("config.json"), "w") as f:
            json.dump(config, f, indent=4)
        show_query_screen(page)
    
    provider_dropdown = ft.Dropdown(
        label="Provider",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        options=[
            ft.dropdown.Option("OpenAI"),
            ft.dropdown.Option("Anthropic"),
            ft.dropdown.Option("OpenRouter")
        ],
        value="OpenRouter",
        color=ft.Colors.BLACK
    )
    api_key_field = ft.TextField(label="API Key", color=ft.Colors.BLACK)
    non_reasoning_field = ft.TextField(label="Non-Reasoning Model", color=ft.Colors.BLACK)
    reasoning_field = ft.TextField(label="Reasoning Model", color=ft.Colors.BLACK)
    submit_button = ft.ElevatedButton("Submit", on_click=on_setup_submit, color=ft.Colors.WHITE)
    
    page.controls.clear()
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Setup Configuration", size=32, weight="bold", color=ft.Colors.BLACK),
                    provider_dropdown,
                    api_key_field,
                    non_reasoning_field,
                    reasoning_field,
                    submit_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                width=400,
                spacing=20,
            ),
            alignment=ft.alignment.center,
            expand=True,
        )
    )
    page.update()

def show_query_screen(page: ft.Page):
    query_field = ft.TextField(
        hint_text="Type your query here...",
        border_color="transparent",
        border_width=0,
        text_size=20,
        text_align = ft.TextAlign.CENTER,
        autofocus=True,
        color=ft.Colors.BLACK
    )
    greeting = ft.Text("Hello, what is your query?", size=32, weight="bold", color=ft.Colors.BLACK)
    
    async def on_query_submit(e):
        await on_query_submitted(query_field.value, page)
    
    query_field.on_submit = on_query_submit
    
    page.controls.clear()
    page.add(
        ft.Column(
            controls=[
                greeting,
                query_field,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            expand=True,
        )
    )
    page.update()

async def on_query_submitted(query: str, page: ft.Page):
    cards.load_images()
    spread_name, card_names = cards.get_spread(query)
    if debug_flag:
        print("Spread:", spread_name, card_names)
    await show_spread_screen(query, spread_name, card_names, page)

async def show_spread_screen(user_query, spread_name, card_names, page: ft.Page):
    left_pane_width = page.width / 2 if page.width else 960
    left_pane_height = page.height - 100 if page.height else 440
    right_pane_width = page.width / 2 if page.width else 960

    def get_card_positions(spread_name, num_cards):
        positions = []
        center_x = 960 // 4
        center_y = 540 // 2
        padding = 20
        if debug_flag:
            print("Creating spread of type: ", spread_name)
        match spread_name:
            case "Employment" | "Self Healing":
                scale_factor = 0.33
                card_width = int(300 * scale_factor)
                card_height = int(527 * scale_factor)
                # top card
                positions.append((center_x, center_y - 1.5*card_height))
                # two cards in center row
                positions.append((center_x - card_width, center_y - 0.5*card_height + padding))
                positions.append((center_x + card_width, center_y - 0.5*card_height + padding))
                # three cards in the bottom row
                positions.append((center_x - 1.75*card_width, center_y + 0.5*card_height + 2*padding))
                positions.append((center_x, center_y + 0.5*card_height + 2*padding))
                positions.append((center_x + 1.75*card_width, center_y + 0.5*card_height + 2*padding))
            case "Straight shooter":
                scale_factor = 0.33
                card_width = int(300 * scale_factor)
                card_height = int(527 * scale_factor)
                # five cards in one row!
                positions.append((center_x - 2*card_width - padding, center_y))
                positions.append((center_x - card_width, center_y))
                positions.append((center_x + padding, center_y))
                positions.append((center_x + card_width + 2*padding, center_y))
                positions.append((center_x + 2*card_width + 3*padding, center_y))
            case "Lucky Horseshoe":
                scale_factor = 0.275
                card_width = int(300 * scale_factor)
                card_height = int(527 * scale_factor)
                # top card
                positions.append((center_x, center_y - 1.5*card_height - padding))
                # two cards in the second row
                positions.append((center_x - 1.5*card_width, center_y - card_height))
                positions.append((center_x + 1.5*card_width, center_y - card_height))
                # two cards in the third row
                positions.append((center_x - 1.5*card_width, center_y + padding))
                positions.append((center_x + 1.5*card_width, center_y + padding))
                # two cards in the fourth row
                positions.append((center_x - 1.5*card_width, center_y + card_height + 2*padding))
                positions.append((center_x + 1.5*card_width, center_y + card_height + 2*padding))
            case "Money Spread":
                scale_factor = 0.33
                card_width = int(300 * scale_factor)
                card_height = int(527 * scale_factor)
                # two cards in top row
                positions.append((center_x - card_width, center_y - 1.5*card_height))
                positions.append((center_x + card_width, center_y - 1.5*card_height))
                # two cards in second row
                positions.append((center_x - card_width, center_y - 0.5*card_height + padding))
                positions.append((center_x + card_width, center_y - 0.5*card_height + padding))
                # bottom card
                positions.append((center_x, center_y + 0.5*card_height + 2*padding))
            case "Obstacle Spread":
                scale_factor = 0.33
                card_width = int(300 * scale_factor)
                card_height = int(527 * scale_factor)
                # one card in the top row, to the left
                positions.append((center_x - 1.75*card_width, center_y - 1.5*card_height))
                # three cards in the middle row
                positions.append((center_x - 1.75*card_width, center_y - 0.5*card_height + padding))
                positions.append((center_x, center_y - 0.5*card_height + padding))
                positions.append((center_x + 1.75*card_width, center_y - 0.5*card_height + padding))
                # one card in the bottom row, to the left
                positions.append((center_x - 1.75*card_width, center_y + 0.5*card_height + 2*padding))
            case "The Blind Spot":
                scale_factor = 0.4
                card_width = int(300 * scale_factor)
                card_height = int(527 * scale_factor)
                # two cards in top row
                positions.append((center_x - 0.5*card_width, center_y - 0.75*card_height))
                positions.append((center_x + 0.5*card_width + padding, center_y - 0.75*card_height))
                # two cards in second row
                positions.append((center_x - 0.5*card_width, center_y + 0.25*card_height + padding))
                positions.append((center_x + 0.5*card_width + padding, center_y + 0.25*card_height + padding))
            case "The Goodbye Spread":
                scale_factor = 0.33
                card_width = int(300 * scale_factor)
                card_height = int(527 * scale_factor)
                # two cards in top row
                positions.append((center_x - 1.5*card_width, center_y - 0.75*card_height))
                positions.append((center_x + 1.5*card_width + padding, center_y - 0.75*card_height))
                # one card in the center
                positions.append((center_x + padding//2, center_y - 0.25*card_height + padding//2))
                # two cards in second row
                positions.append((center_x - 1.5*card_width, center_y + 0.25*card_height + padding))
                positions.append((center_x + 1.5*card_width + padding, center_y + 0.25*card_height + padding))
            case "True Love":
                scale_factor = 0.33
                card_width = int(300 * scale_factor)
                card_height = int(527 * scale_factor)
                # two cards in the top row, from the left
                positions.append((center_x - 1.75*card_width, center_y - 1.5*card_height))
                positions.append((center_x, center_y - 1.5*card_height))
                # three cards in the middle row
                positions.append((center_x - 1.75*card_width, center_y - 0.5*card_height + padding))
                positions.append((center_x, center_y - 0.5*card_height + padding))
                positions.append((center_x + 1.75*card_width, center_y - 0.5*card_height + padding))
                # one card in the bottom row, to the left
                positions.append((center_x - 1.75*card_width, center_y + 0.5*card_height + 2*padding))
            case "Love General":
                scale_factor = 0.33
                card_width = int(300 * scale_factor)
                card_height = int(527 * scale_factor)
                # first row - three cards with one-card gaps
                positions.append((center_x - 2*card_width - padding, center_y - 0.75*card_height))
                positions.append((center_x + padding, center_y - 0.75*card_height))
                positions.append((center_x + 2*card_width + 3*padding, center_y - 0.75*card_height))
                # second row - two cards between the gaps
                positions.append((center_x - card_width, center_y - 0.25*card_height + padding//2))
                positions.append((center_x + card_width + 2*padding, center_y - 0.25*card_height + padding//2))
                # last row - one card below the center card of the first row
                positions.append((center_x + padding, center_y + 0.25*card_height + padding))
            case "Overall Health Read":
                scale_factor = 0.33
                card_width = int(300 * scale_factor)
                card_height = int(527 * scale_factor)
                # three cards in the top row
                positions.append((center_x - 1.75*card_width, center_y - 1.5*card_height))
                positions.append((center_x, center_y - 1.5*card_height))
                positions.append((center_x + 1.75*card_width, center_y - 1.5*card_height))
                # one card in the middle row
                positions.append((center_x, center_y - 0.5*card_height + padding))
                # one card in the bottom row
                positions.append((center_x, center_y + 0.5*card_height + 2*padding))

            case _:
                error("Unrecognized Spread Type!")
        return (scale_factor, positions)

    scale_factor, positions = get_card_positions(spread_name, len(card_names))
    card_display_width = int(300 * scale_factor)
    card_display_height = int(527 * scale_factor)
    
    card_widgets = []
    for i, front in enumerate(card_names):
        pos_x, pos_y = positions[i]
        pos_x = pos_x
        pos_y = pos_y
        flip_delay = 0.5 * i
        card = CardWidget(front_image_url=front, width=card_display_width, height=card_display_height, flip_delay=flip_delay)
        card_widgets.append(
            ft.Container(
                content=card,
                left=pos_x,
                top=pos_y
            )
        )
    left_card_container = ft.Stack(
        controls=card_widgets,
        width=left_pane_width,
        height=left_pane_height,
        expand=False,
    )

    def exit_app(e):
        page.window.close()
        sys.exit()
    
    buttons_row = ft.Row(
        controls=[
            ft.ElevatedButton(
                "Restart",
                on_click=lambda e: show_query_screen(page),
                style=ft.ButtonStyle(color=ft.Colors.WHITE)
            ),
            ft.ElevatedButton(
                "Quit",
                on_click=lambda e: exit_app(e),
                style=ft.ButtonStyle(color=ft.Colors.WHITE)
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )
    left_pane = ft.Column(
        controls=[
            left_card_container,
            buttons_row,
            ft.Container(
                content=ft.Text(spread_name, size=18, color=ft.Colors.BLACK),
                alignment=ft.alignment.bottom_left,
                expand=True
            )
        ],
        spacing=10,
        expand=True
    )

    loader_row = ft.Row(
        controls=[
            ft.ProgressRing(width=30, height=30),
            ft.Text("Loading response...", size=20, color=ft.Colors.BLACK)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    response_text = ft.Text("", size=18, color=ft.Colors.BLACK)
    response_container = ft.Container(
    content=ft.Column([loader_row, response_text], scroll=ft.ScrollMode.ALWAYS),
    expand=True,
    border=ft.border.all(1, ft.Colors.BLACK),
    padding=10,
    width=right_pane_width,
    height=page.height - 150 if page.height else 900)

    further_query = ft.TextField(
        hint_text="Enter further query...",
        border_color="transparent",
        border_width=0,
        text_size=18,
        width=right_pane_width - 20
    )
    async def further_query_submit(e):
        response_text.visible = False
        loader_row.visible = True
        page.update()
        answer = await asyncio.to_thread(cards.further_query, response_text.value, further_query.value)
        response_text.value += "\n\n" + answer
        loader_row.visible = False
        response_text.visible = True
        page.update()

    further_query.on_submit = further_query_submit
    right_pane = ft.Column(
        controls=[
            response_container,
            further_query
        ],
        spacing=10,
        expand=True
    )
    main_row = ft.Row(
        controls=[left_pane, right_pane],
        expand=True,
        spacing=10
    )
    page.controls.clear()
    page.add(main_row)
    page.update()

    long_text = await asyncio.to_thread(cards.divine, user_query, spread_name, card_names)
    response_text.value = long_text
    loader_row.visible = False
    page.update()

class CardWidget(ft.Container):
    def __init__(self, front_image_url: str, width: int, height: int, flip_delay: float, **kwargs):
        super().__init__(width=width, height=height, **kwargs)
        self.front_image_url = front_image_url
        self.back_image_url = cards.resource_path("backcover.png")
        self.flipped = False
        self.content = ft.Image(src=self.back_image_url, width=width, height=height, fit=ft.ImageFit.COVER)
        self.controls = [self.content]
        asyncio.create_task(self.flip_after_delay(flip_delay))
    
    async def flip_after_delay(self, delay: float):
        await asyncio.sleep(delay)
        self.flipped = True
        self.content.src = self.front_image_url
        try:
            self.update()
        except AssertionError:
            pass

def main_page(page: ft.Page):
    page.title = "SeerGPT"
    page.bgcolor = ft.Colors.WHITE
    page.window_width = 1920
    page.window_height = 1080

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLACK,
            on_primary=ft.Colors.WHITE,
            background=ft.Colors.WHITE,
            on_background=ft.Colors.BLACK,
        )
    )
    
    if not validate_config():
        show_setup_screen(page)
    else:
        show_query_screen(page)

def main():
    ft.app(target=main_page)

if __name__ == "__main__":
    main()
