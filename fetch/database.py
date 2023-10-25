from json import loads
from requests import get


class Database:
    def __init__(
            self, page='http://www.themealdb.com/api/json/v1/1/'
    ):

        self.page = page


    def send_req(
            self, req
        ):

        return get(
            req
        )


    def make_details(
            self, response,
            request
        ):

        details = [

        ]

        keys = list(
            response['meals'][0].keys()
        )

        values = list(
            response['meals'][0].values()
        )

        for i in range(len(values)):
            data = [
                keys[i - 1].lower().replace('str', ''), values[i - 1]
            ]

            if (data[1] in ['', ' ']
                or data[1] is None):

                continue

            if ("ingredient" in data[0]):

                data[0] = data[0].replace(
                    'ingredient', 'ingredient '
                )

            if ("measure" in data[0]):

                data[0] = data[0].replace(
                    'measure', 'measure of ingredient '
                )

            details.append(
                data
            )

        del request, response, values, keys
        return details


    def random_meal(
            self
        ):

        request = f"{self.page}random.php"

        response = loads(
            self.send_req(
                request
            ).content.decode()
        )

        if (response
            and response['meals'] is not None):

            return self.make_details_random(
                response, request
            )

        del request, response
        return 0


    def make_details_random(
            self, response,
            request
        ):

        return self.make_details(
            response, request
        )


    def get_details(
            self, id
        ):

        return self.make_request('lookup.php?i=', id)


    def make_details_by_parameters(
            self, response,
            request
        ):

        return self.make_details(
            response, request
        )


    def by_ingredient(
            self, ingredient
        ):

        meals_return = [

        ]

        request = f"{self.page}filter.php?i={ingredient.replace(' ', '_').lower()}"

        return self.return_meals(
            request, meals_return
        )


    def categories(
            self
        ):

        data = loads(
            self.send_req(
                'http://www.themealdb.com/api/json/v1/1/categories.php'
            ).content.decode()
        )['categories']

        categories_list = [
            category['strCategory'] for category in data
        ]

        return sorted(
            categories_list
        )


    def by_category(
            self, category
        ):

        meals_return = [

        ]

        request = f"{self.page}filter.php?c={category}"

        return self.return_meals(
            request, meals_return
        )


    def by_name(
            self, name
        ):

        return self.make_request('search.php?s=', name)


    def make_request(
            self, arg0,
            arg1
        ):

        request = f"{self.page}{arg0}{arg1}"

        response = loads(
            self.send_req(
                request
            ).content.decode()
            )

        if (response
            and response['meals'] is not None):

            return self.make_details_by_parameters(
                response, request
            )

        del request, response
        return 0


    def return_meals(
            self, request,
            meals_return
        ):

        response = loads(
            self.send_req(
                request
            ).content.decode()
        )

        if (response
            and response['meals'] is not None):

            return self.extend_data(
                response, meals_return,
                request
                )

        del request, response, meals_return
        return 0


    def extend_data(
            self, response,
            meals_return, request
        ):

        meals = response['meals']

        meals_return.extend(
            [
                int(meal['idMeal']),
                meal['strMeal']
            ]
            for meal in meals
        )

        del request, response, meals

        return meals_return

