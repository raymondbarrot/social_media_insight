import xlsxwriter
from dateutil import parser


def create_workbook(file_name):
    fb_workbook = xlsxwriter.Workbook(file_name)
    return fb_workbook


def fb_add_worksheet(fb_workbook, fb_posts, ws_name):
    fb_worksheet = fb_workbook.add_worksheet(ws_name)

    fb_worksheet.write(0, 0, 'Date Posted')
    fb_worksheet.write(0, 1, 'Post Link')

    row = 1
    counter = 0

    for fb_post in fb_posts:
        date_posted = parser.parse(fb_post['created_time'])
        fb_worksheet.write(row, 0, date_posted.strftime("%m/%d/%Y"))
        fb_worksheet.write(row, 1, fb_post['permalink_url'])
        row += 1
        counter += 1

    fb_worksheet.write(row, 0, 'Total Count: ' + str(counter))


def ig_add_worksheet(ig_workbook, ig_posts, ws_name):
    ig_worksheet = ig_workbook.add_worksheet(ws_name)

    ig_worksheet.write(0, 0, 'Date Posted')
    ig_worksheet.write(0, 1, 'Post Link')

    row = 1
    counter = 0

    for ig_post in ig_posts:
        date_posted = parser.parse(ig_post['timestamp'])
        ig_worksheet.write(row, 0, date_posted.strftime("%m/%d/%Y"))
        ig_worksheet.write(row, 1, ig_post['permalink'])
        row += 1
        counter += 1

    ig_worksheet.write(row, 0, 'Total Count: ' + str(counter))


# old version / unused
def export_excel(fb_posts, ws_name):
    fb_workbook = xlsxwriter.Workbook('fb_posts.xlsx')
    fb_worksheet = fb_workbook.add_worksheet(ws_name)

    fb_worksheet.write(0, 0, 'Date Posted')
    fb_worksheet.write(0, 1, 'Post Link')

    row = 1
    counter = 0

    print('Loop FB Posts')
    for fb_post in fb_posts:
        date_posted = parser.parse(fb_post['created_time'])
        fb_worksheet.write(row, 0, date_posted.strftime("%m/%d/%Y"))
        fb_worksheet.write(row, 1, fb_post['permalink_url'])
        row += 1
        counter += 1

    fb_worksheet.write(row, 0, 'Total Count: ' + str(counter))
    fb_workbook.close()
