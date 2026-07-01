import json

from django.core.management.base import BaseCommand
from django.db import transaction

from insurance.models import Package, CoverageOption


class Command(BaseCommand):
    help = "Loads package records from records.json into database."

    def handle(self, *args, **kwargs):
        try:
            with open(
                "./insurance/management/commands/records.json",
                "r",
                encoding="utf-8",
            ) as file:
                record = json.load(file)

            with transaction.atomic():
                # Create packages
                packages = [
                    Package(**package) for package in record["insurance_package"]
                ]
                Package.objects.bulk_create(packages)

                # Create coverage options
                coverage_options = [
                    CoverageOption(**coverage)
                    for coverage in record["insurance_coverageoption"]
                ]
                CoverageOption.objects.bulk_create(coverage_options)

                # Create many-to-many relationships
                through_model = Package.coverage_options.through

                m2m_relations = [
                    through_model(
                        package_id=relation["package_id"],
                        coverageoption_id=relation["coverageoption_id"],
                    )
                    for relation in record["insurance_package_coverage_options"]
                ]

                through_model.objects.bulk_create(m2m_relations)

                self.stdout.write(
                    self.style.SUCCESS("Records loaded into database successfully.")
                )

        except Exception as ex:
            print("Exception:")
            print(ex)
