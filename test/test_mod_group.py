from model.formfiller import Group
import random




def test_modify_group_name(app, db, json_groups):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = json_groups
    old_group = random.choice(old_groups)
    group.id = old_group.id
    app.group.modify_group_by_id(id, group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


