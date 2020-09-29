from hstest.test_case import TestCase

from base import HyperJobTest


class HyperJobTestRunner(HyperJobTest):
    def generate(self):
        return [
            # 1 task
            TestCase(attach=self.check_server),
            TestCase(attach=self.check_create_vacancies),
            TestCase(attach=self.check_create_resumes),
            # 2 task
            TestCase(attach=self.check_greeting),
            TestCase(attach=self.check_links),
            # 3 task
            TestCase(attach=self.check_vacancies),
            TestCase(attach=self.check_resumes),
            # 4 task
            TestCase(attach=self.check_signup),
            TestCase(attach=self.check_login),
            # 5 task
            TestCase(attach=self.check_create_resume_from_profile),
            TestCase(attach=self.check_forbid_to_create_vacancy),
            TestCase(attach=self.check_forbid_anonymous_create),
        ]

    def check(self, reply, attach):
        return attach()


if __name__ == '__main__':
    import os
    os.environ['HYPERSKILL_TESTS_WITH_SQLITE3'] = '1'
    HyperJobTestRunner('hyperjob.manage').run_tests()
