# -*- coding: utf-8 -*-
"""Command Line Interface for {{ cookiecutter.project_name }}"""
import argparse


def _init_args():
    parser = argparse.ArgumentParser(
        description="Do something useful.")
    args = parser.parse_args()
    return args
