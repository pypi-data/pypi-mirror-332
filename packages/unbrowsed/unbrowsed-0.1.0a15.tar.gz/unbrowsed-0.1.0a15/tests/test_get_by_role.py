import pytest

from unbrowsed import (
    MultipleElementsFoundError,
    NoElementsFoundError,
    get_by_role,
    parse_html,
)


def test_get_by_role_link():
    html = """
    <a href="https://example.com">Example Link</a>
    <button>Button</button>
    """
    dom = parse_html(html)
    assert get_by_role(dom, "link")

    html = """
    <a href="#anchor" aria-current="true">
      <span>The text</span>
    </a>
    """
    dom = parse_html(html)
    assert get_by_role(dom, "link", current=True)

    html = """
    <a href="#anchor" aria-current="true">
      <span>The text</span>
    </a>
    """
    dom = parse_html(html)
    assert get_by_role(dom, "link", current="true")

    html = """
    <a href="#anchor" aria-current="page">
      <span>The text</span>
    </a>
    """
    dom = parse_html(html)
    assert get_by_role(dom, "link", current="page")


def test_get_by_role_button():
    html = """
    <button id="main-button">Regular Button</button>
    <input type="submit" value="Submit Button">
    """
    dom = parse_html(html)

    assert get_by_role(dom, "button")


def test_get_by_role_with_attributes():
    html = """
    <a href="https://example.com" aria-current="true">Current Link</a>
    <a href="https://example.org">Other Link</a>
    """
    dom = parse_html(html)

    assert get_by_role(dom, "link", current="true")

    assert get_by_role(dom, "link", current=True)


def test_get_by_role_no_match():
    html = """
    <div>Some content</div>
    <p>Some paragraph</p>
    """
    dom = parse_html(html)

    with pytest.raises(NoElementsFoundError):
        get_by_role(dom, "button")


def test_get_by_role_multiple_matches():
    html = """
    <button>Button 1</button>
    <button>Button 2</button>
    """
    dom = parse_html(html)

    with pytest.raises(MultipleElementsFoundError) as exc:
        get_by_role(dom, "button")
    assert (
        "Found 2 elements with role 'button'. "
        "Use get_all_by_role if multiple matches are expected."
        == str(exc.value)
    )


def test_get_by_role_prioritize_child():
    html = """
    <nav>
        <a href="https://example.com">Link inside navigation</a>
    </nav>
    """
    dom = parse_html(html)

    link = get_by_role(dom, "link")
    assert link.element.tag == "a"


def test_by_role_input():
    html = """
    <input type="checkbox">
    """
    dom = parse_html(html)
    assert get_by_role(dom, "checkbox")

    html = """
    <input type="radio">
    """
    dom = parse_html(html)
    assert get_by_role(dom, "radio")

    html = """
    <input type="text">
    """
    dom = parse_html(html)
    assert get_by_role(dom, "textbox")


def test_by_role_meter():
    html = """
        <td><meter value="100">100%</meter></td>
        """
    dom = parse_html(html)
    assert get_by_role(dom, "meter").to_have_attribute("value", "100")


def test_by_role_group():
    html = """
    <form>
      <fieldset name="the name">
        <legend>Choose your favorite monster</legend>

        <input type="radio" id="kraken" name="monster" value="K" />
        <label for="kraken">Kraken</label><br />

        <input type="radio" id="sasquatch" name="monster" value="S" />
        <label for="sasquatch">Sasquatch</label><br />

        <input type="radio" id="mothman" name="monster" value="M" />
        <label for="mothman">Mothman</label>
      </fieldset>
    </form>
    """
    dom = parse_html(html)
    assert get_by_role(dom, "group").to_have_attribute("name", "the name")
    assert get_by_role(dom, "group", name="Choose your favorite monster")

    html = """
    <form>
      <fieldset>
        <input type="radio" id="kraken" name="monster" value="K" />
        <label for="kraken">Kraken</label><br />

        <input type="radio" id="sasquatch" name="monster" value="S" />
        <label for="sasquatch">Sasquatch</label><br />

        <input type="radio" id="mothman" name="monster" value="M" />
        <label for="mothman">Mothman</label>
      </fieldset>
    </form>
    """
    dom = parse_html(html)
    with pytest.raises(NoElementsFoundError):
        get_by_role(dom, "group", name="Choose your favorite monster")
