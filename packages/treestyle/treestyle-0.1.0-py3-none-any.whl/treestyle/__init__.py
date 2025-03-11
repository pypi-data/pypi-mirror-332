# Set version ----
from importlib.metadata import version as _v

__version__ = _v("treestyle")

del _v

# Main code ----
from typing import Any


class Formatter:
    n_spaces = 3
    icon_block = "█─"
    icon_pipe = "├─"
    icon_endpipe = "└─"
    icon_connector = "│ "
    string_truncate_mark = " ..."

    def __init__(self, string_max_length: int = 50, max_depth=999, compact=False):
        self.string_max_length = string_max_length
        self.max_depth = max_depth
        self.compact = compact

    @staticmethod
    def get_field_value(obj, k) -> Any:
        raise NotImplementedError()

    @staticmethod
    def fields(node) -> list[str]:
        raise NotImplementedError()

    def format(self, call, depth=0, pad=0):
        """Return a Symbolic or Call back as a nice tree, with boxes for nodes."""

        # call = transform(call)

        crnt_fields = self.fields(call)

        if crnt_fields is None:
            str_repr = repr(call)
            if len(str_repr) > self.string_max_length:
                return str_repr[: self.string_max_length] + self.string_truncate_mark

            return str_repr

        call_str = self.icon_block + call.__class__.__name__

        # short-circuit for max depth ----
        if depth >= self.max_depth:
            return call_str + self.string_truncate_mark

        # format arguments ----
        fields_str = []
        for name in crnt_fields:
            val = self.get_field_value(call, name)

            # either align subfields with the end of the name, or put the node
            # on a newline, so it doesn't have to be so indented.
            if self.compact:
                sub_pad = pad
                linebreak = "\n" if self.fields(val) else ""
            else:
                sub_pad = len(str(name)) + self.n_spaces
                linebreak = ""

            # do formatting
            formatted_val = self.format(val, depth + 1, pad=sub_pad)
            fields_str.append(f"{name} = {linebreak}{formatted_val}")

        padded = []
        for ii, entry in enumerate(fields_str):
            is_final = ii == len(fields_str) - 1

            chunk = self.fmt_pipe(entry, is_final=is_final, pad=pad)
            padded.append(chunk)

        return "".join([call_str, *padded])

    def fmt_pipe(self, x, is_final=False, pad=0):
        if not is_final:
            connector = self.icon_connector if not is_final else "  "
            prefix = self.icon_pipe
        else:
            connector = "  "
            prefix = self.icon_endpipe

        connector = "\n" + " " * pad + connector
        prefix = "\n" + " " * pad + prefix
        # NOTE: because visiting is depth first, this is essentially prepending
        # the text to the left.
        return prefix + connector.join(x.splitlines())
