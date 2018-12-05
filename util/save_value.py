# -*- coding: utf-8 -*-

def saveSetsOfList(check_list, save_key, **check_key):
	'''
	check_list(list): members
	save_key(str): uuid
	check_key: { "status": 1, "team_member_status": 1}
	'''
	expected_list = []

	for i in check_list:
		if all(item in i.items() for item in check_key.items()):
			expected_list.append(i[save_key])

	return expected_list


if __name__ == '__main__':
    check_list = [
        {
            "project_uuid": "8yhRWBazTSENROnp",
            "issue_type_uuid": "PVRsTwjE"
        },
        {
            "project_uuid": "8yhRWBazCr4qrk0t",
            "issue_type_uuid": "PVRsTwjE"
        },
        {
            "project_uuid": "8yhRWBazVGvgKVul",
            "issue_type_uuid": "PVRsTwjE"
        }
    ]
    save_key = "issue_type_uuid"
    a = saveSetsOfList(check_list, save_key, project_uuid = "8yhRWBazCr4qrk0t")
    print a
