def test_normal_case_1():
        assert reverse_string('Hello!') == '!olleH'

def test_normal_case_2():
        assert reverse_string('a man a plan panama') == 'amanap nalp a nam'

def test_normal_case_3():
        assert reverse_string('testing testing 123') == '321 gnitset gnitset'

def test_edge_case_1():
#test empty string
        assert reverse_string('') == ''

def test_edge_case_2():
#test single character string
        assert reverse_string('g') == ('g')

def test_edge_case_3():
#test two character string
        assert reverse_string('yo') = 'oy'

def test_normal_case_1():
        assert reverse_string_recursion('Hello!') == '!olleH'

def test_normal_case_2():
        assert reverse_string_recursion('a man a plan panama') == 'amanap nalp a nam'

def test_normal_case_3():
        assert reverse_string_recursion('testing testing 123') == '321 gnitset gnitset'

def test_edge_case_1():
#test empty string
        assert reverse_string_recursion('') == ''

def test_edge_case_2():
#test single character string
        assert reverse_string_recursion('g') == ('g')

def test_edge_case_3():
#test two character string
        assert reverse_string_recursion('yo') = 'oy'