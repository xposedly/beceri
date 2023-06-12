-----------------------------------------------------------------------------------------------------------------------
// Boþ Bir Yere Ekle:
ACMD(do_select_skill_group)
{
	if(!ch || !ch->IsPC())
		return;
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1)
		return;
	BYTE group;
	str_to_number(group, arg1);
	if (group == 0 || group > 2)
		return;
	ch->SelectSkillGroupWithWindow(group);
}
-----------------------------------------------------------------------------------------------------------------------
