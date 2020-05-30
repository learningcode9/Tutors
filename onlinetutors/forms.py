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
MONTH_CHOICES=(
    ("1","January"),
    ("2","February"),
    ("3","March"),
    ("4","April"),
    ("5","May"),
    ("6","June"),
    ("7","July"),
    ("8","August"),
    ("9","September"),
    ("10","October"),
    ("11","November"),
    ("12","December"),
)
DAY_CHOICES=(
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
    ("11","11"),
    ("12","12"),
    ("13","13"),
    ("14","14"),
    ("15","15"),
    ("16","16"),
    ("17","17"),
    ("18","18"),
    ("19","19"),
    ("20","20"),
    ("21","21"),
    ("22","22"),
    ("23","23"),
    ("24","24"),
    ("25","25"),
    ("26","26"),
    ("27","27"),
    ("28","28"),
    ("29","29"),
    ("30","30"),
    ("31","31"),
                        
)


class application(forms.Form):
    firstName=forms.CharField(max_length=30)
    lastName=forms.CharField(max_length=30)
    Email=forms.EmailField()
    phonenumber=forms.IntegerField(max_value=11)
    password=forms.PasswordInput()
    confirm_password=forms.PasswordInput()
    address1=forms.CharField()
    address2=forms.CharField()
    state=forms.ChoiceField(choices=STATE_CHOICES)
    city=forms.ChoiceField()
    zipcode=forms.IntegerField()
    month=forms.ChoiceField(choices=month)
