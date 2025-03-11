import ast
import inspect
import functools
from typing import Callable, Dict, Any

import astunparse

from astrologic.decorators.base import BaseDecorator
from astrologic.function_text import FunctionText


class TailRecursionOptimization(BaseDecorator):
    @staticmethod
    def add_prefix_and_postfix(function_text, original_function):
        prefix = """def superfunction(*args, **kwargs):
    is_recursion = False
"""
        postfix = f"""    while True:
        result = {original_function.__name__}(*args, **kwargs)
        if not is_recursion:
            return result
        is_recursion = False
        args, kwargs = result""".replace('\t', function_text.indent_symbols)
        function_text.wrapp_clean_text(prefix=prefix, postfix=postfix, indent=1)

    def get_new_return_node(self, node):
        args = node.value.args
        kwargs = node.value.keywords
        dict_keys = [ast.Constant(value=keyword.arg) for keyword in kwargs]
        dict_values = [keyword.value for keyword in kwargs]
        new_node = ast.Return(
            value=ast.Tuple(
                elts=[
                    ast.Tuple(elts=args, ctx=ast.Load()),
                    ast.Dict(
                        keys=dict_keys,
                        values=dict_values,
                    ),
                ], ctx=ast.Load(),
            ), ctx=ast.Load(),
        )
        return new_node

    def is_recursion(self, function_name: str, node: ast.AST) -> bool:
        try:
            return node.value.func.id == function_name

        except Exception:
            return False

    def convert_tree_to_function(self, tree: ast.AST, original_function: Callable[..., Any], namespace: Dict[str, Any], debug_mode_on: bool) -> Callable[..., Any]:
        if debug_mode_on:
            print('---------------------')
            print(f'Function {original_function.__name__} from module {original_function.__module__} changed. Its code is roughly equivalent to the following:')
            print(astunparse.unparse(tree))
            print('---------------------')

        tree = ast.fix_missing_locations(tree)
        code = compile(tree, filename=inspect.getfile(original_function), mode='exec')
        exec(code, namespace)
        result: Callable[..., Any] = namespace['superfunction']
        result = functools.wraps(original_function)(result)
        return result

    def change_tree(self, tree: ast.AST, original_function: Callable[..., Any], function_text: FunctionText, *args: Any, **kwargs: Any):
        self.add_prefix_and_postfix(function_text, original_function)
        tree = ast.fix_missing_locations(self.get_source_tree(function_text))

        class RewriteName(ast.NodeTransformer):
            def visit_Return(_self, node):
                if self.is_recursion(original_function.__name__, node):
                    _nonlocal = ast.Nonlocal(names=['is_recursion'])
                    flag = ast.Assign(targets=[ast.Name(id='is_recursion', ctx=ast.Store())], value=ast.Constant(value=True))
                    new_return_node = self.get_new_return_node(node)
                    return [_nonlocal, flag, new_return_node]
                return node

        return RewriteName().visit(tree)


no_recursion = TailRecursionOptimization()
