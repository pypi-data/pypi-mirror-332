from pycoze import utils


socket = utils.socket


class WebCls:
    def get_simplified_webpage(self, url: str) -> str:
        return socket.post_and_recv_result(
            "getSimplifiedWebpage", {"url": url}
        )
    
    def get_simplified_html(self, html: str) -> str:
        return socket.post_and_recv_result(
            "getSimplifiedHtml", {"html": html}
        )