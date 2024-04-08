

rss_url_tpl="https://rsshub.app/twitter/user/{tw_username}/readable=1&authorNameBold=1&showAuthorInTitle=1&showAuthorInDesc=1&showQuotedAuthorAvatarInDesc=1&showAuthorAvatarInDesc=1&showEmojiForRetweetAndReply=1&showRetweetTextInTitle=0&addLinkForPics=1&showTimestampInDescription=1&showQuotedInTitle=1&heightOfPics=150"

def generate_rss_feed(tw_username):
    return rss_url_tpl.format(tw_username=tw_username)


if __name__ == '__main__':
    print(generate_rss_feed('ton_economic'))
