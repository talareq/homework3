from model.formfiller import Group
import pytest

def test_add_group(app, db, json_groups):
        group = json_groups
        with pytest.allure.step('Given a group_list'):
                old_groups = db.get_group_list()
        with pytest.allure.step('When I add a new group %s to the list' % group):
                app.group.create(group)
        with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
                new_groups = db.get_group_list()
                old_groups.append(group)
                assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


