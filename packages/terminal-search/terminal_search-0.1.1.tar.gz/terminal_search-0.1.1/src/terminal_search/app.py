from .search import Search
from textual import on, work
from textual.widget import Widget
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Input, ContentSwitcher, ListView, ListItem, Static, Switch, Link, Label
from textual.containers import Horizontal, VerticalScroll, Vertical

class TerminalSearch(App):
    """A Textual app for searching the web in the terminal"""

    BINDINGS = [("d", "toggle_dark", "toggle dark mode"), ("q", "quit", "quit"), ("c", "clear_search", "clear search"), ("b", "back_to_search", "back to search page"), ("r", "back_to_results", "back to results page (if available)")]

    CSS_PATH = "main.tcss"

    def __init__(self):
        super().__init__()
        self.search = Search()
        self.search_query = ""
        self.results = []
        self.title = "Terminal Search"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        yield Header(show_clock=True, icon="🔎")
        yield Footer()
        with ContentSwitcher(initial="search"):
            with Horizontal(id="search"):
                with VerticalScroll():
                    yield Input(placeholder="enter search query", id="search-input")
                    with Horizontal():
                        yield Button("search", id="search-button", variant="primary")
                        yield Button("settings", id="settings-button", variant="default")
                        yield Link(text="GitHub", url="https://github.com/CragglesG/terminal-search", id="github-link")
            with VerticalScroll(id="results"):
                yield ListView(id="results-list")
            with VerticalScroll(id="settings"):
                yield Static("[b]settings", classes="label")
                with Horizontal():
                    yield Static("always use neural search:    ", classes="label")
                    yield Switch(value=False, id="type")
                with Horizontal():
                    yield Static("moderation:    ", classes="label")
                    yield Switch(value=False, id="moderation")
            yield VerticalScroll(id="contents")

    @on(Button.Pressed)
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == None:
            return
        elif self.search_query != "" and event.button.id == "search-button":
            event.button.loading = True
            self.perform_search()
        elif event.button.id == "settings-button":
            self.query_one(ContentSwitcher).current = "settings"
        elif "result" in event.button.id:
            event.button.loading = True
            self.perform_get(event.button)

    @work(exclusive=True, thread=True)
    def perform_search(self) -> None:
        try:
            results = self.search.search(self.search_query)
            self.call_from_thread(self.switch_to_results, results)
        except ValueError as e:
            self.notify(f"Sorry, we had trouble finding results for your search. Try rephrasing your query or changing settings.", severity="error", title="No Results Found")
            self.call_from_thread(self.turn_off_loading, self.query_one("#search-button"))
        except Exception as e:
            self.notify(f"An unexpected error occurred: {e}", severity="error", title="Unexpected Error")
            self.call_from_thread(self.turn_off_loading, self.query_one("#search-button"))

    @work(exclusive=True, thread=True)
    def perform_get(self, button: Button | Widget) -> None:
        url = self.results[int(button.id.split("-")[1])].url
        try:
            contents = self.search.get(url)
            self.call_from_thread(self.switch_to_contents, contents, button)
        except ValueError as e:
            self.notify(f"Sorry, we had trouble finding the contents of this webpage.", severity="error", title="No Contents Found")
            self.call_from_thread(self.turn_off_loading, button)
        except Exception as e:
            self.notify(f"An unexpected error occurred: {e}", severity="error", title="Unexpected Error")
            self.call_from_thread(self.turn_off_loading, button)

    def turn_off_loading(self, widget: Widget):
        widget.loading = False

    def switch_to_results(self, results):
        self.results = results
        self.query_one("#search-button").loading = False

        list_view = self.query_one("#results-list")
        list_view.clear()
        for i, result in enumerate(self.results):
            list_view.append(ListItem(Button(result.title, id=f"result-{i}"), Link(result.url, classes="url")))

        self.query_one(ContentSwitcher).current = "results"

    async def switch_to_contents(self, contents, button: Button | Widget):
        self.contents = contents
        button.loading = False

        contents_page = self.query_one("#contents")
        await contents_page.mount(VerticalScroll(Static("[b]summary", classes="label"),
            Label(contents.summary, classes="summary", markup=False),
            id="contents-list"))

        self.sub_title = contents.title

        self.query_one(ContentSwitcher).current = "contents"

    @on(Input.Submitted)
    def on_input_submitted(self, event: Input.Submitted) -> None:
        if self.search_query != "":
            button = self.query_one("#search-button")
            button.loading = True
            self.perform_search()

    @on(Input.Changed)
    def on_input_changed(self, event: Input.Changed) -> None:
        self.search_query = event.value

    @on(Switch.Changed)
    def on_switch_changed(self, event: Switch.Changed) -> None:
        if event.switch.id == "moderation":
            self.search.moderation = event.value
        elif event.switch.id == "type":
            self.search.type = "neural" if event.value else "auto"

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_clear_search(self) -> None:
        self.search_query = ""
        self.query_one(ContentSwitcher).current = "search"
        self.query_one(Input).value = ""
        self.query_one(Input).focus()

    def action_back_to_search(self) -> None:
        self.query_one(ContentSwitcher).current = "search"

    def action_back_to_results(self) -> None:
        cs = self.query_one(ContentSwitcher)
        if not self.query("#contents-list") and self.query("#result-0"):
            cs.current = "results"
        elif self.query("#result-0"):
            cs.current = "results"
            self.query_one("#contents-list").remove()
        else:
            self.notify("You haven't searched for anything yet.")
        self.sub_title = ""

def main():
    app = TerminalSearch()
    app.run()

if __name__ == "__main__":
    main()
