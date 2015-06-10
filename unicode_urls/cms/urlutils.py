import re

# checks validity of absolute / relative url
any_path_re = re.compile(
    '^/?[\w.-]+(/[\w.-]+)*/?$',
    re.U)
