"""Work with compact Qt row ranges; expand indexes only when needed."""


def selected_row_count(selection):
    return sum(span.height() for span in selection.selection() if span.left() == 0)


def selected_rows(selection):
    model = selection.model()
    for span in selection.selection():
        if span.left() == 0:
            parent = span.parent()
            for row in range(span.top(), span.bottom() + 1):
                yield model.index(row, 0, parent)
