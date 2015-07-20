from app import db, models

def increase_count(StudentID):
    user = models.Counter.query.filter_by(Student_id=StudentID).all()
    temp_count = 0
    if user is None:
        user = models.Counter(Student_id=StudentID, count=1)
        db.session.add(user)
        db.session.commit()
    else:
        user = models.Counter.query.filter_by(Student_id=StudentID).first_or_404()
        user.count += 1
        temp_count = user.count
        db.session.commit()

    return 'Count: ' + str(temp_count)
