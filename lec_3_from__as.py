from lec_3_my_module import earth_mass as em
from lec_3_my_module import gravity_constant as gvc
from lec_3_my_module import sigma_steff_bolc as sigma

g = 500 * gvc / 10 ** 2
print(g)

x = em * gvc * sigma
print(x)
