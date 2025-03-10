#
#   MIT License
#   
#   Copyright (c) 2024, Mattias Aabmets
#   
#   The contents of this file are subject to the terms and conditions defined in the License.
#   You may not use, modify, or distribute this file except in compliance with the License.
#   
#   SPDX-License-Identifier: MIT
#
from typing import List
from pathlib import Path
from semver import Version
from rich.prompt import Confirm
from rich.console import Console
from typing_extensions import Annotated
from typer import Typer, Option
from devtools_cli.models import *
from devtools_cli.utils import *
from .helpers import *
from .models import *


app = Typer(
	name="version",
	no_args_is_help=True,
	help="Manages project version number and tracks filesystem changes."
)
console = Console(soft_wrap=True)


NameOpt = Annotated[str, Option(
	'--name', '-n', show_default=False, help=''
	'A unique name identifier of the trackable component to reference it by.'
)]
TargetOpt = Annotated[str, Option(
	'--target', '-t', show_default=False, help=''
	'The path to target with tracking, relative to the path of the .devtools config file.'
)]
IgnoreOpt = Annotated[List[str], Option(
	'--ignore', '-i', show_default=False, help=''
	'A path to be ignored relative to the target path. Can be used multiple times.'
)]
TrackDescriptorOpt = Annotated[bool, Option(
	'--track-descriptor', '-D', show_default=False, help=''
	'Whether devtools should bump the version number in the project descriptor file. '
	'False by default.'
)]
TrackChartOpt = Annotated[bool, Option(
	'--track-chart', '-C', show_default=False, help=''
	'Whether devtools should bump the version number in the Helm Chart.yaml file. '
	'False by default.'
)]


@app.command(name="track", epilog="Example: devtools version track --name app")
def cmd_track(
		name: NameOpt,
		target: TargetOpt = '.',
		ignore: IgnoreOpt = None,
		track_descriptor: TrackDescriptorOpt = False,
		track_chart: TrackChartOpt = False
) -> None:
	"""
	Tracks changes inside the specified target path using file hashing.
	Defaults to the .devtools config directory if called without 'target' option.
	"""
	config_file: Path = find_local_config_file(init_cwd=True)
	config: VersionConfig = read_local_config_file(VersionConfig)
	track_path = config_file.parent / target

	if not track_path.exists():
		console.print(f"ERROR! Cannot track a target path which does not exist: '{track_path}'\n")
		raise SystemExit()
	elif track_path.is_file() and ignore:
		console.print(f"ERROR! Cannot set ignored paths when target is a file: '{track_path}'\n")
		raise SystemExit()

	index = None
	for i, entry in enumerate(config.components):
		if entry.name == name and entry.target != target:
			console.print(f"ERROR! Cannot assign the same name '{name}' to multiple targets!\n")
			raise SystemExit()
		elif entry.target == target and entry.name != name:
			console.print(f"ERROR! Cannot assign the same target '{target}' to multiple names!\n")
			raise SystemExit()
		elif entry.name == name and entry.target == target and entry.ignore == ignore:
			console.print(f"Nothing to update in the tracked component.\n")
			raise SystemExit()
		elif entry.name == name and entry.target == target:
			index = i

	if track_path.is_file():
		track_hash = digest_file(track_path)
	else:
		track_hash = digest_directory(track_path, ignore)

	if track_descriptor:
		config.app_version = read_descriptor_file_version()
		config.track_descriptor = track_descriptor

	if track_chart:
		chart_ver, app_ver = read_chart_and_app_version()
		if track_descriptor:
			if chart_ver and chart_ver != config.app_version:
				console.print(
					f"ERROR! The 'version' value in the Helm Chart.yaml file must "
					f"match the version number in the project descriptor file!"
				)
				raise SystemExit()
			elif app_ver and app_ver != config.app_version:
				console.print(
					f"ERROR! The 'appVersion' value in the Helm Chart.yaml file must "
					f"match the version number in the project descriptor file!"
				)
				raise SystemExit()
		if all(x is not None for x in [chart_ver, app_ver]) and chart_ver != app_ver:
			console.print(
				f"ERROR! Devtools requires the 'version' and 'appVersion' "
				f"values in the Helm Chart.yaml file to be identical!"
			)
			raise SystemExit()
		config.track_chart = track_chart
		config.app_version = chart_ver or "0.0.0"

	comp = TrackedComponent(
		hash=track_hash,
		target=target,
		ignore=ignore,
		name=name
	)
	if index is None:
		config.components.append(comp)
		msg = f"Successfully tracked component: '{name}'.\n"
	else:
		config.components[index] = comp
		msg = f"Successfully updated the component '{name}'.\n"

	write_local_config_file(config)
	console.print(msg)


@app.command(name="untrack", epilog="Example: devtools version untrack --name app")
def cmd_untrack(name: NameOpt):
	"""
	Un-tracks filesystem changes for a specified component in the project.
	If the specified name is not being tracked, an error will be raised.
	"""
	config: VersionConfig = read_local_config_file(VersionConfig)

	index = None
	for i, entry in enumerate(config.components):
		if entry.name == name:
			index = i
			break

	if index is None:
		console.print("ERROR! Cannot untrack a non-existing component.\n")
		raise SystemExit()

	config.components.pop(index)
	write_local_config_file(config)
	console.print(f"Successfully untracked the component '{name}'.\n")


MajorBumpOpt = Annotated[bool, Option(
	'--major', '-M', show_default=False, help=""
	"Bump the major version number (the 'X' in 'X.Y.Z'). Y and Z are set to zero."
)]
MinorBumpOpt = Annotated[bool, Option(
	'--minor', '-m', show_default=False, help=""
	"Bump the minor version number (the 'Y' in 'X.Y.Z'). X is left untouched, Z is set to zero."
)]
PatchBumpOpt = Annotated[bool, Option(
	'--patch', '-p', show_default=False, help=""
	"Bump the patch version number (the 'Z' in 'X.Y.Z'). X and Y are left untouched."
)]
SuffixOpt = Annotated[str, Option(
	'--suffix', '-s', show_default=False, help=""
	"Append a suffix to the semver string. Example: '-s beta' produces 'X.Y.Z-beta'."
)]
DowngradeOpt = Annotated[bool, Option(
	'--downgrade', '-D', show_default=False, help=""
	"Whether the version number is downgraded instead."
)]
ValueOpt = Annotated[int, Option(
	'--value', '-V', show_default=False, help=""
	"Explicitly assign this value to the chosen version number level."
)]


@app.command(name="bump", epilog="Example: devtools version bump --minor")
def cmd_bump(
		major: MajorBumpOpt = False,
		minor: MinorBumpOpt = False,
		patch: PatchBumpOpt = False,
		suffix: SuffixOpt = '',
		downgrade: DowngradeOpt = False,
		value: ValueOpt = None
) -> None:
	"""
	Increments the version identifier of the project.
	Defaults to patch version if called without version type options.
	"""
	if sum([major, minor, patch]) > 1:
		console.print("ERROR! Cannot bump multiple version numbers at the same time!\n")
		raise SystemExit()
	if not any([major, minor, patch]):
		patch = True

	if count_descriptors() > 1:
		console.print("ERROR! Cannot have multiple language descriptor files in the project directory!\n")
		raise SystemExit()

	config_file = find_local_config_file(init_cwd=True)
	config: VersionConfig = read_local_config_file(VersionConfig)
	descriptor_ver = read_descriptor_file_version()

	desc_ver = Version.parse(descriptor_ver)
	conf_ver = Version.parse(config.app_version)
	ver = desc_ver if desc_ver > conf_ver else conf_ver

	if value:
		new_version = str(Version(
			major=value if major else ver.major,
			minor=value if minor else ver.minor,
			patch=value if patch else ver.patch
		))
	elif downgrade:
		new_version = str(Version(
			major=ver.major - (1 if major else 0),
			minor=ver.minor - (1 if minor else 0),
			patch=ver.patch - (1 if patch else 0)
		))
	else:
		index = [major, minor, patch].index(True)
		func = [ver.bump_major, ver.bump_minor, ver.bump_patch][index]
		new_version = str(func()) + (f"-{suffix}" if suffix else '')

	verb = "Downgrade" if downgrade else "Bump"
	do_action = Confirm.ask(
		f"{verb} the version of [light_goldenrod3]'{config_file.parent.name}'[/] from "
		f"[light_slate_blue]{config.app_version}[/] to [chartreuse3]{new_version}[/]?"
	)
	if not do_action:
		console.print(f"[bold]Did not {verb.lower()} the project version.\n")
		raise SystemExit()

	if config.track_descriptor:
		write_descriptor_file_version(new_version)
	if config.track_chart:
		write_chart_and_app_version(new_version)

	for comp in config.components:
		track_path = config_file.parent / comp.target
		if track_path.is_file():
			track_hash = digest_file(track_path)
		else:
			track_hash = digest_directory(track_path, comp.ignore)
		comp.hash = track_hash

	config.app_version = new_version
	write_local_config_file(config)
	verb = "downgraded" if downgrade else "bumped"
	console.print(f"[bold]Successfully {verb} the project version.\n")


GitHubEnvOpt = Annotated[str, Option(
	'--ghenv', '-e', show_default=False, help=''
	'The name for the variable that is inserted into the GitHub Action environment file.'
)]
GitHubOutOpt = Annotated[str, Option(
	'--ghout', '-o', show_default=False, help=''
	'The name for the variable that is inserted into the GitHub Action outputs file.'
)]


@app.command(name="echo", epilog="Example: devtools version echo")
def cmd_echo(name: NameOpt = '', ghenv: GitHubEnvOpt = '', ghout: GitHubOutOpt = ''):
	"""
	Echoes project version or component hashes to stdout, optionally
	inserts echoed data into GitHub Action files if applicable.
	"""
	config: VersionConfig = read_local_config_file(VersionConfig)
	var_map = [(ghenv, GitHubFile.ENV), (ghout, GitHubFile.OUT)]
	if not name:
		validate_version(config.app_version)
		console.print(config.app_version)
		[
			write_to_github_file(key, config.app_version, file)
			for key, file in var_map if key
		]
		return
	else:
		for entry in config.components:
			validate_digest(entry.hash)
			if entry.name == name:
				console.print(entry.hash)
				[
					write_to_github_file(key, entry.hash, file)
					for key, file in var_map if key
				]
				return
		console.print("ERROR! Cannot access the hash of a non-existent component!\n")
		raise SystemExit()


@app.command(name="regen", epilog="Example: devtools version regen")
def cmd_regen():
	"""
	Regenerates the hashes of all tracked components and updates
	the config file. Does not change the project version.
	"""
	config_file = find_local_config_file(init_cwd=False)
	config: VersionConfig = read_local_config_file(VersionConfig)

	if config_file is None or config.is_default or not config.components:
		console.print("No component hashes to update.\n")
		raise SystemExit()

	for comp in config.components:
		track_path = config_file.parent / comp.target
		if track_path.is_file():
			track_hash = digest_file(track_path)
		else:
			track_hash = digest_directory(track_path, comp.ignore)
		comp.hash = track_hash

	write_local_config_file(config)
	console.print("[bold]Successfully updated component hashes.\n")


BaseVerOpt = Annotated[str, Option(
	"--base", "-b", show_default=False, help=''
	'The base version identifier to compare against.'
)]
HeadVerOpt = Annotated[str, Option(
	"--head", "-h", show_default=False, help=''
	'The head version identifier to compare against.'
)]


@app.command(name="cmp", epilog="Example: devtools version cmp --base 1.0.0 --head 1.0.1")
def cmd_cmp(base: BaseVerOpt, head: HeadVerOpt, ghenv: GitHubEnvOpt = '', ghout: GitHubOutOpt = ''):
	"""
	Returns either "lt", "gt" or "eq" which represents the
	logical relationship between the two version identifiers.
	The comparison is made as: head <operand> base.
	"""
	base_ver = Version.parse(base)
	head_ver = Version.parse(head)

	result = "eq"
	if head_ver < base_ver:
		result = "lt"
	elif head_ver > base_ver:
		result = "gt"

	var_map = [(ghenv, GitHubFile.ENV), (ghout, GitHubFile.OUT)]
	[
		write_to_github_file(key, result, file)
		for key, file in var_map if key
	]
	console.print(result)
