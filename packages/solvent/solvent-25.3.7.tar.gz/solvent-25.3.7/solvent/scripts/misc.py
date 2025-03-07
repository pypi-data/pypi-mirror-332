import random

import pomace

from . import Script


class TommyBryant(Script):
    URL = "https://www.cityoftarrant.com/contact"

    def run(self, page: pomace.Page) -> pomace.Page:
        person = pomace.fake.person

        pomace.log.info(f"Beginning iteration as {person}")
        page.fill_first_name(person.first_name)
        page.fill_last_name(person.last_name)
        page.fill_email(person.email)
        page.fill_comment(
            random.choice(
                [
                    "Tommy Bryant must resign over his racist comments.",
                    "Tommy Bryant's racism doesn't belong in Alabama.",
                    "Get Tommy Bryant out of our city council.",
                    "Tarrant is better than Tommy Bryant. He must go!",
                    "I'm going to keep email the City of Tarrant until Tommy Bryant resigns.",
                ]
            )
        )
        page.fill_captcha("Blue")
        return page.click_submit()

    def check(self, page: pomace.Page) -> bool:
        return "submission has been received" in page


class PatriotPage(Script):
    URL = "https://patriotpage.org"

    def run(self, page: pomace.Page) -> pomace.Page:
        person = pomace.fake.person

        pomace.log.info(f"Beginning iteration as {person}")
        page = page.click_create_an_account()
        page.fill_email(person.email)
        page.fill_confirm_email(person.email)
        page.fill_password(person.password)
        page.fill_confirm_password(person.password)
        page.fill_first_name(person.first_name)
        page.fill_last_name(person.last_name)
        page.fill_nickname(person.nickname)
        page.fill_country("United States")
        page.fill_selection(
            random.choice(
                [
                    "Precinct delegate",
                    "Poll Watcher",
                    "Poll Challenger",
                    "Election Inspector",
                    "Patriot Approved Candidate",
                    "Grassroots Patriot Leader",
                    "Patriot Volunteer",
                ]
            )
        )
        page.browser.execute_script('document.getElementsByTagName("a")[3].remove()')
        page.browser.execute_script('document.getElementsByTagName("a")[3].remove()')
        page.click_agree(wait=0)

        pomace.log.info("Creating account")
        return page.click_create_account(wait=1)

    def check(self, page: pomace.Page) -> bool:
        return "We’re almost there!" in page


class Graydons(Script):
    URL = "https://www.graydonscrossing.com/"

    def run(self, page: pomace.Page) -> pomace.Page:
        person = pomace.fake.person

        subject = random.choice(
            [
                "Concerns About The Well Church",
                "Question About Owner's Church",
                "The Well Church Affiliation",
                "Matthew Fuller and The Well",
                "Question About Inclusivity",
                "Concerns About Discrimination",
                "Disappointed Former Customer",
                "No Longer Supporting",
                "Feedback from Creston Resident",
                "Community Impact Concerns",
            ]
        )

        message = random.choice(
            [
                "I just learned that Matthew Fuller runs The Well Church opposing gay marriage. This will really hurt the welcoming atmosphere that Creston neighborhood is known for. I'm very disappointed.",
                "As a Creston resident, I'm shocked to discover the owner's involvement with The Well Church and their anti-LGBT stance. This goes against everything our inclusive neighborhood stands for.",
                "The Creston neighborhood has always been a diverse and accepting community. Learning about the owner's discriminatory views through The Well Church makes me worry about the impact on our neighborhood.",
                "After hearing about the owner's connection to The Well Church and their anti-LGBT stance, I'm concerned about how this will affect Creston's reputation as a welcoming neighborhood.",
                "The news about Matthew Fuller's anti-LGBT beliefs is disturbing. Creston has been building an inclusive community for years - this feels like a step backwards for our neighborhood.",
                "As someone who lives in Creston, I'm troubled by how Matthew Fuller's stance against marriage equality at The Well Church will impact our neighborhood's welcoming atmosphere.",
                "Your owner's involvement with The Well Church's anti-LGBT message is concerning. This kind of discrimination has no place in Creston - we're known for being open and accepting.",
                "The revelation about Matthew Fuller's anti-gay marriage position through The Well Church has left me worried about Creston's future. Our neighborhood thrives on diversity and inclusion.",
                "I'm disappointed to learn about Matthew Fuller and The Well Church's discriminatory views. Creston has worked hard to be a welcoming place for everyone.",
                "How can Matthew Fuller claim to serve the Creston community while The Well Church holds views that exclude our LGBT neighbors? This will hurt our inclusive culture.",
                "I will be organizing a protest outside your business this weekend regarding Matthew Fuller and The Well Church's discriminatory views. We demand a public response.",
                "Our neighborhood group is planning to boycott until Matthew Fuller addresses The Well Church's anti-LGBT stance. We won't support discrimination.",
                "Expect peaceful demonstrations until The Well Church and Matthew Fuller issue a clear statement about their position on LGBT rights. We deserve transparency.",
                "We're mobilizing residents to protest The Well Church's discriminatory values. Matthew Fuller must address these concerns or face continued action.",
                "Is Graydon's still LGBTQ+ friendly given the owners stance on marriage only being between one man and one woman?",
            ]
        )

        pomace.shared.client.clear_cookies()
        page = page.click_contact_us()

        # Duplication is required for some reason
        page.fill_your_name(person.name, delay=1)
        page.fill_your_name(person.name, delay=1)

        page.fill_your_email(person.email, delay=1)
        page.fill_subject(subject, delay=1)
        page.fill_message(message, delay=1)
        return page.click_submit()

    def check(self, page: pomace.Page) -> bool:
        return "Thank you for your message" in page
