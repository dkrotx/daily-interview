def flatten_dictionary(d):
  flatten = dict()
  def flatten_it(prefix, subd):
      for k, v in subd.items():
          if isinstance(v, dict):
            flatten_it(prefix + k + '.', v)
          else:
            flatten[prefix + k] = v

  flatten_it('', d)
  return flatten

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
