import click

@click.command()
@click.argument('command')
def main(command):
    if command == 'hi':
        click.echo('Miau miau')
    else:
        click.echo(f"Unknown command: {command}")

if __name__ == '__main__':
    main()