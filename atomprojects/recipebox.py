recipes1 = {}
recipes2 = {}

recipe1 = []
ingredients1 = {'graham crackers', 'melted butter', 'sugar'}
instructions1 = ['To make the crust: In a small bowl, mix the cracker crumbs with the melted butter and the sugar together until evenly moistened. ', ' Press the crumb mixture onto the bottom of a 9-inch springform pan. ', 'Bake the crust until golden brown, about 10 to 12 minutes. Cool the pan on a rack.', ]
recipe1.append(ingredients1)
recipe1.append(instructions1)

recipe2 = []
ingredients2 = {'cream cheese', 'sour cream', 'eggs', 'vanilla extract', 'heavy cream'}
instructions2 = [' In the bowl of a standing mixer fitted with the paddle attachment, or with a hand-held mixer, cream the cream cheese on medium speed until smooth. ', 'Gradually add the sugar and beat until light and fluffy. Beat in the sour cream. ', 'Add the eggs, one at a time, beating well after each addition. Stir in the vanilla and cream. Pour the batter into the prepared pan. ', 'Bake until the top of the cheesecake is lightly browned, but the center still jiggles slightly, about 45 minutes. Cool the cake in the pan on a rack. Cover with plastic wrap and refrigerate overnight before serving. ']
recipe2.append(ingredients2)
recipe2.append(instructions2)

recipes1['Cheesecake rust'] = recipe1
print(recipes1)

recipes2['Cheesecake Filling'] = recipe2
print(recipes2)
