import configparser
from dateutil import parser
from file_util import ig_add_worksheet, fb_add_worksheet, create_workbook
from service_util import get_fb_posts_by_date, get_ig_posts_by_date


def fetch_export_fb_posts():
    fb_config = configparser.ConfigParser()
    fb_config.read('config.ini')

    fb_start_list = ['08/1/2022', '09/1/2022', '10/1/2022']
    fb_end_list = ['09/1/2022', '10/1/2022', '11/1/2022']

    fb_access_token = fb_config['fb']['access_token']
    fb_limit = fb_config['fb']['limit']
    fb_page_id = fb_config['fb']['page_id']
    fb_api_version = fb_config['fb']['api_version']

    fb_posts_file = create_workbook('fb_post_new.xlsx')
    i = 0
    for fb_start in fb_start_list:
        print('FB: ' + fb_start)

        fb_url = 'https://graph.facebook.com/' + fb_api_version + '/' + fb_page_id + '/feed?fields=permalink_url,created_time&since=' + fb_start_list[i] + '&until=' + fb_end_list[i] + '&limit=' + fb_limit + '&access_token=' + fb_access_token

        fb_response = get_fb_posts_by_date(fb_url)
        fb_all_posts = fb_response['json_data']['data']

        if 'paging' in fb_response['json_data']:
            while 'next' in fb_response['json_data']['paging']:
                next_url = fb_response['json_data']['paging']['next']
                fb_response = get_fb_posts_by_date(next_url)
                fb_all_posts = fb_all_posts + fb_response['json_data']['data']

        ws_name = parser.parse(fb_start_list[i]).strftime('%B')
        fb_add_worksheet(fb_posts_file, fb_all_posts, ws_name)
        i = i + 1

    fb_posts_file.close()


def fetch_export_ig_posts():
    ig_config = configparser.ConfigParser()
    ig_config.read('config.ini')

    ig_start_list = ['08/1/2022', '09/1/2022']
    ig_end_list = ['09/1/2022', '10/1/2022']

    ig_access_token = ig_config['ig']['access_token']
    ig_limit = ig_config['ig']['limit']
    ig_business_id = ig_config['ig']['ig_business_id']
    ig_api_version = ig_config['ig']['api_version']

    ig_posts_file = create_workbook('ig_post_new.xlsx')
    i = 0
    for ig_start in ig_start_list:
        print('IG: ' + ig_start)

        ig_url = 'https://graph.facebook.com/' + ig_api_version + '/' + ig_business_id + '/media?fields=permalink,timestamp&since=' + ig_start_list[i] + '&until=' + ig_end_list[i] + '&limit=' + ig_limit + '&access_token=' + ig_access_token

        ig_response = get_ig_posts_by_date(ig_url)
        ig_all_posts = ig_response['json_data']['data']

        if 'paging' in ig_response['json_data']:
            while 'next' in ig_response['json_data']['paging']:
                next_url = ig_response['json_data']['paging']['next']
                ig_response = get_fb_posts_by_date(next_url)
                ig_all_posts = ig_all_posts + ig_response['json_data']['data']

        ws_name = parser.parse(ig_start_list[i]).strftime('%B')
        ig_add_worksheet(ig_posts_file, ig_all_posts, ws_name)
        i = i + 1

    ig_posts_file.close()


if __name__ == '__main__':
    print('Processing...')
    fetch_export_fb_posts()
    fetch_export_ig_posts()
    print('Done!')
