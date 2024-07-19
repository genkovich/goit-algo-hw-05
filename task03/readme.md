Для обох патернів пошуку у заданих текстах Article 1 та Article 2 найшвидшим алгоритмом виявився Boyer-Moore. Цей алгоритм демонструє найнижчий час виконання для обох патернів у кожному з текстів.

### Таблиця для патерну "алгоритм":

|  Algorithm  | Pattern  |  Article  | Time (seconds)       |
|-------------|----------|-----------|----------------------|
|  Rabin-Karp | алгоритм | Article 1 | 0.006531189996167086 |
|  Rabin-Karp | алгоритм | Article 2 | 0.009560689999489114 |
|     KMP     | алгоритм | Article 1 | 0.003285300001152791 |
|     KMP     | алгоритм | Article 2 | 0.004846708005061373 |
| Boyer-Moore | алгоритм | Article 1 | 0.000024754997866693 |
| Boyer-Moore | алгоритм | Article 2 | 0.000180820999958086 |

### Таблиця для патерну "asdsdsadasdas":

|  Algorithm  |    Pattern    |  Article  | Time (seconds)       |
|-------------|---------------|-----------|----------------------|
|  Rabin-Karp | asdsdsadasdas | Article 1 | 0.007672268002352212 |
|  Rabin-Karp | asdsdsadasdas | Article 2 | 0.009832668998569716 |
|     KMP     | asdsdsadasdas | Article 1 | 0.002707027997530531 |
|     KMP     | asdsdsadasdas | Article 2 | 0.004022925000754185 |
| Boyer-Moore | asdsdsadasdas | Article 1 | 0.000358644996595103 |
| Boyer-Moore | asdsdsadasdas | Article 2 | 0.000503834999108221 |