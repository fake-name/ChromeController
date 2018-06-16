
import logging
import sys
import click

from .Generator import gen
from . import chrome_context

@click.group()
@click.option('--verbose', '-v', is_flag=True, help='''
		The opposite of silent. Causes the internal logging to output \
		all traffic over the chromium control interface. VERY noisy.''')
@click.option('--silent', '-s', is_flag=True, help='''
		Suppress all output aside from the fetched content. \
		This can be used to make ChromeController act like \
		an alternative to curl with proper JS rendering.''')
def cli(verbose, silent):
	'''
ChromeController

\b
Usage: python3 -m ChromeController [-s | --silent] [-v | --verbose]
  python3 -m ChromeController fetch <url> [--binary <bin_name>] [--outfile <out_file_name>]
  python3 -m ChromeController update
  python3 -m ChromeController (-h | --help)
  python3 -m ChromeController --version

\b
Options:
  -s --silent   Suppress all output aside from the fetched content
                This basically makes ChromeController act like a alternative to curl
  -v --verbose  The opposite of silent. Causes the internal logging to output
                all traffic over the chromium control interface. VERY noisy.
  --version     Show version.
  fetch         Fetch a specified URL's content, and output it to the console.
	'''

	if verbose:
		logging.basicConfig(level=logging.DEBUG)
	elif silent:
		logging.basicConfig(level=logging.ERROR)
	else:
		logging.basicConfig(level=logging.INFO)


@cli.command()
def update():
	'''
	Update the generated class
	'''
	gen.update_generated_class(force=True, output_diff=True)

@cli.command()
def version():
	'''
	Print the ChromeController Version
	'''
	print("Version goes here?")

@cli.command()
@click.argument('url', required=True)
@click.option('--binary', '-b', default='google-chrome', help='Specify a specific chromium binary.')
@click.option('--outfile', '-o', default=False, help='''Write the output to a file. \
				Text content will be UTF-8 encoded. \
				Binary content will be written as-is.''')
@click.option('--noprint', '-n', is_flag=True, help='Do not print the fetched file to the console.')
@click.option('--rendered', '-r', is_flag=True, help='Allow the page to render in JS before extracting source.')
def fetch(url, binary, outfile, noprint, rendered):
	'''
	Fetch a specified URL's content, and output it to the console.
	'''
	with chrome_context.ChromeContext(binary=binary) as cr:
		resp = cr.blocking_navigate_and_get_source(url)
		if rendered:
			resp['content'] = cr.get_rendered_page_source()
			resp['binary'] = False
			resp['mimie'] = 'text/html'

	if not noprint:
		if resp['binary'] is False:
			print(resp['content'])
		else:
			print("Response is a binary file")
			print("Cannot print!")

	if outfile:
		with open(outfile, "wb") as fp:
			if resp['binary']:
				fp.write(resp['content'])
			else:
				fp.write(resp['content'].encode("UTF-8"))


if __name__ == '__main__':
	cli()


