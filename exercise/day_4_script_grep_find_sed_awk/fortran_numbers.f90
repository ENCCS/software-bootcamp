program print_number
	implicit none
	integer aa, result
	integer :: bb = 8
	integer(kind=2) :: cc = 12
	integer(4) :: dd = 16

	double precision pi
	parameter(pi = 3.1415926535353)

	complex (kind=8) complex_add, complex_minus, complex_multiply, complex_divide
	complex (kind=8) :: comb = (2.0, 3.4)
	complex comc

	character (len=20) char_a, char_d
	character(10) :: char_b = "yonglei", char_c = "jing"

	logical loa
	logical lob

	print("(1a5, 1f12.6)"), "pi = ", pi

    aa = 5
	print("(1a16, 4x, 4i6)"), "aa, bb, cc, dd =", &
		aa, bb, cc, dd
	
	result = (aa + bb) / cc * dd
	print*, " result = ", result
	print*, ' '

	print*, "calculations about complex numbers"
	comc = (4.5, 6.7) 
	complex_add = comb + comc
	complex_minus = comb - comc
	complex_multiply = comb * comc
	print("(1a31, 6f12.4)"), "results for complex numbers1 = ", complex_add, &
		complex_minus, complex_multiply
	print*, "results for complex numbers2 = ", complex_add, complex_minus, complex_multiply
	print*, ' '

	print*, "output characters"
	char_a = "jingsijingxuan"
	print*, "char_a = ||", char_a, "||, and char_b = ||", char_b, "|| and char_c =||", char_c, "||"
	char_a(6:) = " are in school"
	print*, "char_a = ||", char_a, "||"

	char_a = "jingsi"
	char_b = " and "
	char_c = "jingxuan"
	char_d = char_a(:7)//char_b(:6)//char_c(:8)
	print*, "char_d = ||", char_d, "||"  ! char_d = ||jingsi  and  jingxua||
	print*, ' '

	loa = .true.
	lob = .false.
	print*, "two logical value = ", loa, lob
	print*, ' '

end program print_number
