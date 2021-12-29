from allianceauth.eveonline.models import (
    EveAllianceInfo,
    EveCorporationInfo,
    EveCharacter)
from allianceauth.authentication.models import State
from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from .models import (
    AlumniSetup,
    CharacterCorporationHistory,
    CorporationAllianceHistory)
from .app_settings import ALUMNI_STATE_NAME, ALUMNI_TASK_PRIORITY
from .providers import esi
import datetime

from allianceauth.services.hooks import get_extension_logger
logger = get_extension_logger(__name__)


@shared_task
def run_alumni_check_all():
    for character in EveCharacter.objects.all().values('character_id'):
        alumni_check_character.apply_async(
            args=[character['character_id']], priority=ALUMNI_TASK_PRIORITY
        )


@shared_task
def alumni_check_character(character_id: int) -> bool:
    """Check/Update a characters alumni status using the historical models

    Parameters
    ----------
    character_id: int
        Should match an existing EveCharacter model

    Returns
    -------
    bool
        Whether the user is an alumni or not **it is updated in this function as well**"""

    alumni_setup = AlumniSetup.objects.first()
    alumni_state = State.objects.get(name=ALUMNI_STATE_NAME)
    character = EveCharacter.objects.get(character_id=character_id)

    if character.corporation in alumni_setup.alumni_corporations.all():
        # Cheapo cop-out to end early
        alumni_state.member_characters.add(character)
        return True

    if character.alliance in alumni_setup.alumni_alliances.all():
        # Cheapo cop-out to end early
        alumni_state.member_characters.add(character)
        return True

    char_corp_history = CharacterCorporationHistory.objects.filter(character=character)

    for corp in char_corp_history:
        if corp in alumni_setup.alumni_corporations.all():
            # Cheapo cop-out to end early
            alumni_state.member_characters.add(character)
            return True

    for alliance in alumni_setup.alumni_alliances.all():
        if char_alliance_datecompare(alliance_id=alliance.alliance_id, character_id=character_id):
            alumni_state.member_characters.add(character)
            return True

    # If we reach this point, we aren't an alumni
    alumni_state.member_characters.remove(character)
    return False


def char_alliance_datecompare(alliance_id: int, character_id: int) -> bool:
    """Voodoo relating to checking start dates and _next_ start dates

    Necessary to determine if a character was a member of a corp
    WHILE it was in an alliance

    Parameters
    ----------
    alliance_id: int
        Should match an existing EveAllianceInfo model

    character_id: int
        Should match an existing EveCharacter model

    Returns
    -------
    bool
        Whether True"""

    character = EveCharacter.objects.get(character_id=character_id)
    char_corp_history = CharacterCorporationHistory.objects.filter(character=character).order_by('record_id')

    for index, char_corp_record in enumerate(char_corp_history):
        # Corp Joins Alliance, Between Char Join/Leave Corp
        try:
            filter_end_date = char_corp_history[index+1].start_date
        except IndexError:
            filter_end_date = datetime.datetime.now()

        if CorporationAllianceHistory.objects.filter(corporation_id=char_corp_record.corporation_id,
                                                     alliance_id=alliance_id,
                                                     start_date__range=(char_corp_record.start_date,
                                                                        filter_end_date)).exists() is True:
            return True

        corp_alliance_history = CorporationAllianceHistory.objects.filter(
            corporation_id=char_corp_record.corporation_id)

        for index_2, corp_alliance_record in enumerate(corp_alliance_history):
            # Needs to be unfiltered alliance id because we need _next_ start date
            # but check if the alliance id matches before we run any logic

            if corp_alliance_record.alliance_id == alliance_id:
                # Char Joins Corp, Between Corp Join/Leave
                if corp_alliance_record.start_date < char_corp_record.start_date < corp_alliance_history[index_2+1].start_date:
                    return True
                # Char Leaves Corp, Between Corp Join/Leave
                elif corp_alliance_record.start_date < char_corp_history[index+1].start_date < corp_alliance_history[index_2+1].start_date:
                    return True
                # Corp Leaves Alliance in between Char Join/Leave Corp
                elif char_corp_record.start_date < corp_alliance_history[index_2+1].start_date < char_corp_history[index+1].start_date:
                    return True
                else:
                    return False
            else:
                return False


@shared_task
def update_all_models():
    """Update All Corp/Alliance history models from ESI"""

    for character in EveCharacter.objects.all().values('character_id'):
        update_charactercorporationhistory.apply_async(
            args=[character['character_id']], priority=ALUMNI_TASK_PRIORITY
        )

    for char_corp_record in CharacterCorporationHistory.objects.values('corporation_id').distinct():
        update_corporationalliancehistory.apply_async(
            args=[char_corp_record['corporation_id']], priority=ALUMNI_TASK_PRIORITY
        )


@shared_task
def update_corporationalliancehistory(corporation_id: int):
    """Update CorporationAllianceHistory models from ESI

    Parameters
    ----------
    corporation_id: int """

    try:
        data = esi.client.Corporation.get_corporations_corporation_id_alliancehistory(
            corporation_id=corporation_id).result()
    except Exception as e:
        logger.error(e)
        return

    for dat in data:
        try:
            if dat['is_deleted'] == 'true':
                deleted = True
            else:
                deleted = False
            model = CorporationAllianceHistory(
                corporation_id=corporation_id,
                alliance_id=dat['alliance_id'],
                is_deleted=deleted,
                record_id=dat['record_id'],
                start_date=dat['start_date'],
            )
            model.save()
        except Exception as e:
            logger.error(e)


@shared_task
def update_charactercorporationhistory(character_id: int):
    """Update CharacterCorporationHistory models from ESI

    Parameters
    ----------
    character_id: int
        Should match an existing EveCharacter model"""

    try:
        data = esi.client.Character.get_characters_character_id_corporationhistory(character_id=character_id).result()
    except Exception as e:
        logger.error(e)
        return

    try:
        character = EveCharacter.objects.get(character_id=character_id)
    except Exception as e:
        logger.error(e)
        return

    for dat in data:
        try:
            if dat['is_deleted'] == 'true':
                deleted = True
            else:
                deleted = False

            model = CharacterCorporationHistory(
                character=character,
                corporation_id=dat['corporation_id'],
                is_deleted=deleted,
                record_id=dat['record_id'],
                start_date=dat['start_date'],
            )
            model.save()
        except Exception as e:
            logger.error(e)
