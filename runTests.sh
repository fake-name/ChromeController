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

nosetests                            \
	--with-coverage                  \
	--exe                            \
	--cover-package=ChromeController \
	--stop                      \
	tests.test_header_overrides
	# tests
	# --nocapture                      \
	# tests.test_xhr_get
	# tests.test_post
	# tests.test_tab_pool

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

coverage report --show-missing

coverage erase

