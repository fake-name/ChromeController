#!/bin/bash


# Test ALL THE THINGS

set -e

# nosetests                            \
# 	--with-coverage                  \
# 	--exe                            \
# 	--cover-package=ChromeController \
# 	tests.test_simple

# nosetests                            \
# 	--with-coverage                  \
# 	--exe                            \
# 	--cover-package=ChromeController \
# 	--nocapture                      \
# 	tests.test_header_overrides


# nosetests                            \
# 	--with-coverage                  \
# 	--exe                            \
# 	--cover-package=ChromeController \
# 	tests.test_redirects

# pytest                            \
# 	--with-coverage                  \
# 	--exe                            \
# 	--cover-package=ChromeController \
# 	--stop                      \
# 	tests
# 	# tests.test_header_overrides
# 	# --nocapture                      \
# 	# tests.test_xhr_get
# 	# tests.test_post
# 	# tests.test_tab_pool

# pytest --exitfirst  --log-cli-level=DEBUG
pytest --exitfirst

# nosetests                            \
# 	--with-coverage                  \
# 	--exe                            \
# 	--cover-package=ChromeController \
# 	tests

	# tests.test_multithreaded
	# --nocapture                \
	# tests.test_waf_bullshit.TestPreemptiveWrapper
	# tests.test_waf_bullshit
	# --with-cprofile \
	# tests.test_simple
	# tests.test_selenium

# coverage report --show-missing

# coverage erase

