from unittest import TestCase, main
from social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self):
        self.sm = SocialMedia('momo', "YouTube", 100, 'any')

    def test_init(self):
        self.assertEqual('momo', self.sm._username)
        self.assertEqual('YouTube', self.sm._platform)
        self.assertEqual('any', self.sm._content_type)
        self.assertEqual(100, self.sm.followers)
        self.assertEqual([], self.sm._posts)

    def test_platform_with_invalid_platform(self):
        valid_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(Exception) as ex:
            self.sm.platform = 'FB'
        self.assertEqual(f"Platform should be one of {valid_platforms}", str(ex.exception))

    # def test_platform_with_valid_platform(self):
    #     valid_platforms = ['Instagram', 'YouTube', 'Twitter']
    #

    def test_negative_followers(self):
        with self.assertRaises(Exception) as ex:
            self.sm.followers = -2
        self.assertEqual("Followers cannot be negative.", str(ex.exception))

    def test_create_post_append_new_post(self):
        self.assertEqual(len(self.sm._posts), 0)
        my_post = 'This is my new post'
        new_post = {'content': my_post, 'likes': 0, 'comments': []}

        self.sm.create_post(my_post)
        self.assertEqual(len(self.sm._posts), 1)
        self.assertEqual(new_post, self.sm._posts[0])

    def test_create_post_return_message(self):
        my_new_post = 'This is my new post'
        result = "New any post created by momo on YouTube."
        self.assertEqual(result, self.sm.create_post(my_new_post))

    def test_like_post_invalid_post_index(self):
        my_post = 'This is my new post'
        self.sm.create_post(my_post)
        self.assertEqual("Invalid post index.", self.sm.like_post(3))

    def test_like_post_likes_equal_to_ten(self):
        my_post = 'This is my new post'
        self.sm.create_post(my_post)
        self.sm._posts[0]['likes'] = 10
        self.assertEqual("Post has reached the maximum number of likes.", self.sm.like_post(0))

    def test_like_post_correct_increment(self):
        my_post = 'This is my new post'
        self.sm.create_post(my_post)
        self.sm._posts[0]['likes'] = 3
        self.sm.like_post(0)
        self.assertEqual(4, self.sm._posts[0]['likes'])
        self.assertEqual("Post liked by momo.", self.sm.like_post(0))

    def test_comment_on_post_if_comment_larger_than_ten(self):
        my_post = 'This is my new post'
        self.sm.create_post(my_post)
        post = self.sm._posts[0]

        comment = 'This is my new comment'
        self.assertEqual("Comment added by momo on the post.",
                         self.sm.comment_on_post(0, comment))
        # self.assertEqual(len(self.sm._posts['comment']), 1)

    def test_comment_on_post_if_comment_shorter_than_ten(self):
        my_post = 'This is my new post'
        self.sm.create_post(my_post)
        post = self.sm._posts[0]

        comment = 'Hi'
        self.assertEqual("Comment should be more than 10 characters.",
                         self.sm.comment_on_post(0, comment))


if __name__ == '__main__':
    main()
