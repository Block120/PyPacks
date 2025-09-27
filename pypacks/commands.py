"""
Commands module for PyPacks.
"""


_current_commands = []

def say(text):
	_current_commands.append(f"say {text}")

def _reset_commands():
	global _current_commands
	_current_commands = []


