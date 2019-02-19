.PHONY: clean data lint requirements sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

BUCKET = rajk-data-challenges
PROFILE = default

## Upload Data to S3
sync_data_to_s3:
ifeq (default,$(PROFILE))
	aws s3 sync data_sources/ s3://$(BUCKET)/data_sources/
else
	aws s3 sync data_sources/ s3://$(BUCKET)/data_sources/ --profile $(PROFILE)
endif

## Download Data from S3
sync_data_from_s3:
ifeq (default,$(PROFILE))
	aws s3 sync s3://$(BUCKET)/data_sources/ data_sources/
else
	aws s3 sync s3://$(BUCKET)/data_sources/ data_sources/ --profile $(PROFILE)
endif
