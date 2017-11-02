def gen_fn():
    result = yield 1
    print('result of yield: {}'.format(result))
    result2 = yield 2
    print('result of 2nd yield: {}'.format(result2))
    return 'done'


gen = gen_fn()

print('pointer_offset:%d , code_pos:%d', gen.gi_frame.f_lasti, len(gen.gi_code.co_code))

print(gen.send(None))
print(gen.gi_frame.f_lasti)

gen.send('hello')

print('pointer_offset:%d , code_pos:%d %s',
      gen.gi_frame.f_lasti,
      len(gen.gi_code.co_code),
      gen.gi_frame.f_locals
  )