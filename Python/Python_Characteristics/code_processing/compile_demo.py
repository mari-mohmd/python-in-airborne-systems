"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : compile_demo.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate the compilation 
              process of the Abstract Syntax Tree (AST) in Python
 Usage      : python compile_demo.py
===============================================================================
"""

import ast

# This AST is the same as the one produced by 'ast_demo.py'.
# In this example, we compile and execute the AST representation of that function.

ast_code = ast.Module(
    body=[
        ast.FunctionDef(
            name='double',
            args=ast.arguments(
                posonlyargs=[],
                args=[
                    ast.arg(arg='x')],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                ast.Return(
                    value=ast.BinOp(
                        left=ast.Name(id='x', ctx=ast.Load()),
                        op=ast.Mult(),
                        right=ast.Constant(value=2)))],
            decorator_list=[]),

        ast.Expr(
            value=ast.Call(
                func=ast.Name(id='print', ctx=ast.Load()),
                args=[
                    ast.Call(
                        func=ast.Name(id='double', ctx=ast.Load()),
                        args=[
                            ast.Constant(value=5)],
                        keywords=[])],
                keywords=[]))],
    type_ignores=[])

ast_code = ast.fix_missing_locations(ast_code)

compiled_code = compile(ast_code, filename='<ast>', mode='exec')
exec(compiled_code)
