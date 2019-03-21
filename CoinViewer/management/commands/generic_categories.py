from django.core.management.base import BaseCommand, CommandError
from CoinViewer.models import RatingCategory


class Command(BaseCommand):
    help = "generates the 8 basic rating categories"

    def handle(self, *args, **options):
        R1 = RatingCategory.objects.create(
            category_name="Price",
            pos_name="Bullish",
            neg_name="Bearish",
            priority=1,
            tooltip="Do you think the price of this coin will increase or decrease in the short term? Bullish means you think it will increase, bearish means you think it will decrease.",
        )
        R1.save()

        R1 = RatingCategory.objects.create(
            category_name="Riskiness",
            pos_name="Safe",
            neg_name="Risky",
            priority=1,
            tooltip="Each coin encompasses different risks depending on many different factors. After doing your own research, do you think this coin represents a safe or risky position?",
        )
        R1.save()

        R1 = RatingCategory.objects.create(
            category_name="Team",
            pos_name="Reputable",
            neg_name="Unproven",
            priority=2,
            tooltip="The team behind a coin is vital to its success. Have you verified the team members on LinkedIn? Are their profiles real? Do they have experience in their technological area? Do you see activity on their GitHub?",
        )
        R1.save()

        R1 = RatingCategory.objects.create(
            category_name="Popularity",
            pos_name="Rising",
            neg_name="Falling",
            priority=3,
            tooltip="There are many coins with developers that are intentionally quiet to keep hype down. On the other hand, some teams try to be vocal to build hype. Do you see this coin gaining or losing popularity in the short term?",
        )
        R1.save()

        R1 = RatingCategory.objects.create(
            category_name="Community",
            pos_name="Levelheaded",
            neg_name="Immature",
            priority=4,
            tooltip="How is the quality of this coin's community? Is it a levelheaded community that permits rational discussion and debate about the coin? Or is it an immature community that doesn't tolerate discussion or criticism?",
        )
        R1.save()

        R1 = RatingCategory.objects.create(
            category_name="Recent News",
            pos_name="Positive",
            neg_name="Negative",
            priority=4,
            tooltip="News is one of the few things within cryptocurrency that creates major price action for many coins. Does the recent news around the coin reflect it in a positive or negative light?",
        )
        R1.save()

        R1 = RatingCategory.objects.create(
            category_name="Feasibility",
            pos_name="Feasible",
            neg_name="Unfeasible",
            priority=5,
            tooltip="We hear a lot of talk in cryptocurrency of what the future holds. There are some big claims being made by teams about efficency, power consumption, and other metrics. Are these claims feasible? Or are they moonshots?",
        )
        R1.save()

        R1 = RatingCategory.objects.create(
            category_name="Usage",
            pos_name="Genuine",
            neg_name="Speculative",
            priority=5,
            tooltip="How is the coin being used? Are people genuinely using it for its intended use case? Or are people mostly holding onto it for speculative purposes?",
        )
        R1.save()
