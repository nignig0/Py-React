def createApp(component, filename):
    content = f"""
        <html>
            <title> Py-React Demo</title>
            <body>
                {component.render()}
            </body>
        </html>
    """

    #write to file
    with open(filename, 'w') as f:
        f.write(content)
        f.close()
    