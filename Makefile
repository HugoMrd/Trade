##
## EPITECH PROJECT, 2023
## B-CNA-410-PAR-4-1-trade-hugo.mouraud
## File description:
## Makefile
##

SRC	=	trade.py

NAME = trade

all: $(NAME)

$(NAME):
	cp $(SRC) $(NAME) && chmod 777 $(NAME)

fclean:
	rm -f $(NAME)

re: fclean all