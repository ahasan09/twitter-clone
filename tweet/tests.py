from django.test import TestCase

from tweet.models import Tweet
from twitteruser.models import TwitterUser


class TweetModelTests(TestCase):
    def setUp(self):
        self.user = TwitterUser.objects.create_user(
            username='alice', password='test-pass-123')
        self.mentioned = TwitterUser.objects.create_user(
            username='bob', password='test-pass-123')

    def test_str_returns_body(self):
        tweet = Tweet.objects.create(body='Hello world', user=self.user)
        self.assertEqual(str(tweet), 'Hello world')

    def test_parse_mentions_finds_existing_users(self):
        tweet = Tweet.objects.create(
            body='Hi @bob and @nonexistent', user=self.user)
        mentions = tweet.parse_mentions()
        self.assertQuerySetEqual(mentions, [self.mentioned])

    def test_ordering_newest_first(self):
        first = Tweet.objects.create(body='first', user=self.user)
        second = Tweet.objects.create(body='second', user=self.user)
        self.assertEqual(list(Tweet.objects.all()), [second, first])
