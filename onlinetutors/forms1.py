from django import forms


STATE_CHOICES =( 
    ("1","Alabama"),("2","Alaska"),("3","Arizona"),("4","Arkansas"),("5","California"),("6","Colorado"),
    ("7","Connecticut"),("8","Delaware"),("9","Florida"),("10","Georgia"),("11","Hawaii"),("12","Idaho"),
    ("13","Illinois"),("14","Indiana"),("15","Iowa"),("16","Kansas"),("17","Kentucky"),("18","Louisiana"),
    ("19","Maine"),("20","Maryland"),("21","Massachusetts"),("22","Michigan"),("23","Minnesota"),("24","Mississippi"),
    ("25","Missouri"),("26","Montana"),("27","Nebraska"),("28","Nevada"),("29","New Hampshire"),("30","New Jersey"),
    ("31","New Mexico"),("32","New York"),("33","North Carolina"),("34","North Dakota"),("35","Ohio"),
    ("36","Oklahoma"),("37","Oregon"),("38","Pennsylvania"),("39","Rhode Island"),("40","South Carolina"),
    ("41","South Dakota"),("42","Tennessee"),("43","Texas"),("44","Utah"),("45","Vermont"),("46","Virginia"),
    ("47","Washington"),("48","West Virginia"),("49","Wisconsin"),("50","Wyoming"),
                                
) 
# MONTH_CHOICES=(
#      ("1","January"),("2","February"),("3","March"),("4","April"),("5","May"),("6","June"),("7","July"),
#      ("8","August"),("9","September"),("10","October"),("11","November"),("12","December"),
#  )
# DAY_CHOICES=(
#      ("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),
#      ("11","11"),("12","12"),("13","13"),("14","14"),("15","15"),("16","16"),("17","17"),("18","18"),
#      ("19","19"),("20","20"),("21","21"),("22","22"),("23","23"),("24","24"),("25","25"),("26","26"),
#      ("27","27"),("28","28"),("29","29"),("30","30"),("31","31"),
#  )

# YEAR_CHOICES=(
#      ("1960","1960"),("1961","1961"),("1962","1962"),("1963","1963"),("1964","1964"),("1965","1965"),
#      ("1966","1966"),("1967","1967"),("1968","1968"),("1969","1969"),("1970","1970"),("1971","1971"),                    
#      ("1972","1972"),("1973","1973"),("1974","1974"),("1975","1975"),("1976","1976"),("1977","1977"),
#      ("1978","1978"),("1979","1979"),("1980","1980"),("1981","1981"),("1982","1982"),("1983","1983"),
#      ("1984","1984"),("1985","1985"),("1986","1986"),("1987","1987"),("1988","1988"),("1989","1989"),     ("1990","1990"),("1991","1991"),("1992","1992"),("1993","1993"),("1994","1994"),("1995","1995"),
#      ("1996","1996"),("1997","1997"),("1998","1998"),("1999","1999"),("2000","2000"),("2001","2001"),
#  )
GENDER_CHOICES=(
     ('male','Male'),
     ('female','Female'),
 )
k=(
    ('yes','Yes'),
    ('no','No'),
)
degree=(
    ('yes','Yes'),
    ('no','No'),
)
classroom=(
    ('yes','Yes'),
    ('no','No'),
)
genres=(
    ('Classical','Classical'),
    ('Rock','Rock'),
    ('Musical Theater','Musical Theater'),
    ('Country','Country'),
    ('Blues','Blues'),
    ('Christian Contemporary','Christian Contemporary'),
    ('Gospel','Gospel'),
    ('Other','Other'),
)

languages=(
    ('English','English'),
    ('Spanish','Spanish'),
    ('German','German'),
    ('Chinese','Chinese'),
    ('Hindi','Hindi'),
    ('French','French'),
    ('Russian','Russian'),
    ('Turkish','Turkish'),
)

class application(forms.Form):
    firstName=forms.CharField(max_length=50,error_messages = { 'required':"Please Enter your firstName"})
    lastName=forms.CharField(max_length=50,error_messages = { 'required':"Please Enter your LastName"})
    Email=forms.EmailField(error_messages = { 'required':"Please Enter email"})
    phonenumber=forms.CharField(max_length=11,error_messages = { 'required':"Please Enter your phoneNumber"})
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    address1=forms.CharField()
    address2=forms.CharField()
    state=forms.ChoiceField(choices=STATE_CHOICES)
    city=forms.CharField()
    zipcode=forms.IntegerField()
    # month=forms.ChoiceField(choices=MONTH_CHOICES)
    # day=forms.ChoiceField(choices=DAY_CHOICES)
    # year=forms.ChoiceField(choices=YEAR_CHOICES)
    DOB=forms.DateField(widget = forms.SelectDateWidget) 
    Gender= forms.CharField(label='Gender',widget=forms.RadioSelect(choices=GENDER_CHOICES))
    k=forms.CharField(label="Have you taught in K-12 schools?",widget=forms.RadioSelect(choices=k))
    degree=forms.CharField(label="Do you have a 4 year degree?",widget=forms.RadioSelect(choices=degree))
    classroom=forms.CharField(label="Have you taught in a classroom setting?",widget=forms.RadioSelect(choices=classroom))
    genres=forms.CharField(label="What genres / styles do you want to teach with Arts in CT?",widget=forms.CheckboxSelectMultiple(choices=genres))
    languages=forms.CharField(label="What languages do you speak?",widget=forms.CheckboxSelectMultiple(choices=languages))
    
    
    