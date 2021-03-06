

class HtmOutput:
    def __init__(self):
        self.datas = []

    def save(self):
        output = open("..\output\output.html", 'w', encoding='utf-8')
        output.write("<html>")
        output.write("<body>")
        output.write("<table>")

        for data in self.datas:
            print('title : '+data['title'])
            output.write("<tr>")
            output.write("<td>%s</td>" % data['url'])
            output.write("<td>%s</td>" % data['title'])
            output.write("<td>%s</td>" % data['summary'])
            output.write("</tr>")

        output.write("</table>")
        output.write("</body>")
        output.write("</html>")

    def append(self, htm_data):
        if htm_data is not None:
            self.datas.append(htm_data)

