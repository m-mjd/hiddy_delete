from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse


def get_id(session, target_uuid, admin_panel_url):
    try:
        response = session.get(admin_panel_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        uuid_tags = soup.find_all('td', {'class': 'col-uuid'})

        user_id = None
        for uuid_tag in uuid_tags:
            if uuid_tag.span.text.strip() == target_uuid:
                user_id = uuid_tag.find_previous(
                    'input', {'name': 'id'})['value']
                break

        return user_id
    except requests.RequestException as e:
        return f"Error during get_id: {e}"


def parse_url(link):
    try:
        parsed_url = urlparse(link)
        domain = parsed_url.scheme + "://" + parsed_url.netloc
        proxy_path = parsed_url.path.split("/")[1]
        admin_id = parsed_url.path.split("/")[2]
        return domain, proxy_path, admin_id
    except Exception as e:
        return f"Error during parse_url: {e}"


def get_csrf_token(session, url):
    try:
        response = session.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        form = soup.find('form', {'id': 'action_form'})
        csrf_token_input = form.find('input', {'name': 'csrf_token'})
        csrf_token = csrf_token_input['value'] if csrf_token_input else None
        return csrf_token
    except requests.RequestException as e:
        return f"Error during get_csrf_token: {e}"


def delete_user_by_id(session, link_panel, user_id):
    try:
        url = f'{link_panel}/admin/user/delete/'

        domain, proxy_path, admin_id = parse_url(link_panel)

        user_url = f'{link_panel}/admin/user/'

        csrf_token = get_csrf_token(session, user_url)

        form_data = {
            'id': user_id,
            'url': f'{domain}{proxy_path}/{admin_id}/admin/user/',
            'csrf_token': csrf_token,
        }

        response = session.post(url, data=form_data)
        response.raise_for_status()

        if response.status_code == 200:
            return f'The user was deleted successfully.'
        else:
            return f'Error code: {response.status_code}'
    except requests.RequestException as e: 
        return f"Error during delete_user_by_id: {e}"