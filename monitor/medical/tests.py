from medical.models import *
from django.db.models import Q

def test_query(my_srb:int, sex = None):
    fer_marker = Marker.objects.filter(name="Ферритин").first()
    fer_marker_condition = MarkerCondition.objects.filter(name=fer_marker).first()
    deviations = fer_marker_condition.deviations
    normal_conditions = deviations.normal.all()
    moderate_conditions = deviations.moderate.all()
    marked_conditions = deviations.marked.all()
    critical_conditions = deviations.critical.all()
    if check_condition(normal_conditions, my_srb, sex):
        return normal_conditions[0].indicators_type
    elif check_condition(moderate_conditions, my_srb, sex):
        return moderate_conditions[0].indicators_type
    elif check_condition(marked_conditions, my_srb, sex):
        return marked_conditions[0].indicators_type
    elif check_condition(critical_conditions, my_srb, sex):
        return critical_conditions[0].indicators_type
    else:
        return "Неизвестно"

    
    
def check_condition(conditions:list, value, sex = None):
    result = []
    print(conditions)
    if sex:
        print(sex)
        if sex == "M":
            conditions = conditions.filter(~Q(sex="Муж")).all()
        else:
            conditions = conditions.filter(~Q(sex="Муж")).all()
    print(conditions)
    for condition in conditions:
        print(condition.__str__())
        indicator = condition.indicator
        print(condition.condition_type, condition.condition_type == ">")
        if condition.condition_type == ">":
            r = value > indicator 
        elif condition.condition_type == "<":
            r = value < indicator 
        elif condition.condition_type == "<=":
            r = value <= indicator 
        elif condition.condition_type == ">=":
            r = value >= indicator 
        else:
            r = value == indicator 
        result.append(r)
    return all(result)


