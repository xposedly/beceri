-----------------------------------------------------------------------------------------------------------------------
// Arat: (case POINT_LEVEL: 'in içinde')
			PointChange(POINT_NEXT_EXP,	GetNextExp(), false);
// Üstüne Ekle:
			if (GetLevel() >= 5 && GetSkillGroup() == 0)
				ChatPacket(CHAT_TYPE_COMMAND, "open_select_skill_window %d", GetJob());
-----------------------------------------------------------------------------------------------------------------------
// En Alta Ýn Yapýþtýr:
void CHARACTER::SelectSkillGroupWithWindow(BYTE group)
{
	if (!IsPC() || GetSkillGroup() != 0)
		return;
	SetSkillGroup(group);
	SetHorseLevel(SKILL_MAX_LEVEL);
	for (int i = 0; i < SKILL_MAX_NUM; i++)
	{
		if (true == CanUseSkill(i))
		{
			switch(i)
			{
				case SKILL_COMBO:
					SetSkillLevel(i, 2);
					break;
				case SKILL_LEADERSHIP:
				case SKILL_POLYMORPH:
					SetSkillLevel(i, 40);
					break;
				case SKILL_LANGUAGE1:
				case SKILL_LANGUAGE2:
				case SKILL_LANGUAGE3:
					SetSkillLevel(i, 20);
					break;
				case SKILL_HORSE_SUMMON:
					SetSkillLevel(i, 10);
					break;
				case SKILL_HORSE:
					SetSkillLevel(i, HORSE_MAX_LEVEL);
					break;
				case SKILL_HORSE_WILDATTACK:
				case SKILL_HORSE_CHARGE:
				case SKILL_HORSE_ESCAPE:
				case SKILL_HORSE_WILDATTACK_RANGE:
					SetSkillLevel(i, 20);
					break;
				default:
					SetSkillLevel(i, 20);
					break;
			}
		}
		else
		{
			switch(i)
			{
			case SKILL_HORSE_WILDATTACK:
			case SKILL_HORSE_CHARGE:
			case SKILL_HORSE_ESCAPE:
			case SKILL_HORSE_WILDATTACK_RANGE:
				SetSkillLevel(i, 20);
				break;
			}
		}
	}
	SetHorseLevel(HORSE_MAX_LEVEL);
	ComputePoints();
	SkillLevelPacket();
}
-----------------------------------------------------------------------------------------------------------------------
