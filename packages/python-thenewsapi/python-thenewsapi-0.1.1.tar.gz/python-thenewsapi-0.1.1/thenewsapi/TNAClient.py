import requests
from thenewsapi import const
from thenewsapi.TNAException import TheNewsAPIException
from thenewsapi.utils import date_to_string

class TheNewsAPIClient(object):
    
    def __init__(self, api_token):
        self.api_token = api_token
        
    def get_top_stories(self,
        search=None,
        search_fields=None,
        locale=None,
        categories=None,
        exclude_categories=None,
        domains=None,
        exclude_domains=None,
        source_ids=None,
        exclude_source_ids=None,
        language=None,
        published_before=None,
        published_after=None,
        published_on=None,
        sort=None,
        limit=None,
        page=None
    ):
        # Payload
        payload = {}
        
        # Search and search fields
        if search is not None:
            if isinstance(search, str):
                payload['search'] = search
            else:
                raise ValueError('Payload search must be string')
        
        if search_fields is not None:
            for _ in search_fields:
                if _ not in const.FIELDS:
                    raise ValueError('Field is not valid')
            
            if isinstance(search_fields, list):
                payload['search_fields'] = ','.join(search_fields)
            elif isinstance(search_fields, str):
                payload['search_fields'] = search_fields
            else:
                raise ValueError('Payload search_fields must be list')
                
        # Locales
        if locale is not None:
            for _ in locale:
                if _ not in const.LOCALES:
                    raise ValueError('Locale is not valid')
                
            if isinstance(locale, list):
                payload['locale'] = ','.join(locale)
            elif isinstance(locale, str):
                payload['locale'] = locale
            else:
                raise ValueError('Payload locale must be list')
                
        # Categories        
        if categories is not None:
            if isinstance(categories, list):
                for _ in categories:
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['categories'] = ','.join(categories)
            elif isinstance(categories, str):
                for _ in categories.split(','):
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['categories'] = categories
            else:
                raise ValueError('Payload categories must be list')
        
        if exclude_categories is not None:
            if isinstance(exclude_categories, list):
                for _ in exclude_categories:
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['exclude_categories'] = ','.join(exclude_categories)
            elif isinstance(exclude_categories, str):
                for _ in exclude_categories.split(','):
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['exclude_categories'] = exclude_categories
            else:
                raise ValueError('Payload exclude_categories must be list')
        
        # Domains
        if domains is not None:
            if isinstance(domains, list):
                payload['domains'] = ','.join(domains)
            elif isinstance(domains, str):
                payload['domains'] = domains
            else:
                raise ValueError('Payload domains must be list')
                
        if exclude_domains is not None:
            if isinstance(exclude_domains, list):
                payload['exclude_domains'] = ','.join(exclude_domains)
            elif isinstance(exclude_domains, str):
                payload['exclude_domains'] = exclude_domains
            else:
                raise ValueError('Payload exclude_domains must be list')
               
        # Source IDs        
        if source_ids is not None:
            if isinstance(source_ids, list):
                payload['source_ids'] = ','.join(source_ids)
            elif isinstance(source_ids, str):
                payload['source_ids'] = source_ids
            else:
                raise ValueError('Payload source_ids must be list')
                
        if exclude_source_ids is not None:
            if isinstance(exclude_source_ids, list):
                payload['exclude_source_ids'] = ','.join(exclude_source_ids)
            elif isinstance(exclude_source_ids, str):
                payload['exclude_source_ids'] = exclude_source_ids
            else:
                raise ValueError('Payload exclude_source_ids must be list')
        
        # Languages
        if language is not None:
            if isinstance(language, list):
                for _ in language:
                    if _ not in const.LANGUAGES:
                        raise ValueError('Category is not valid')
                payload['language'] = ','.join(language)
            elif isinstance(language, str):
                for _ in language.split(','):
                    if _ not in const.LANGUAGES:
                        raise ValueError('Category is not valid')
                payload['language'] = language
            else:
                raise ValueError('Payload language must be list')
        
        # Published methods | NOTE : Only YYYY-MM-DD and YYYY-MM-DDTHH:MM:SS supported right now
        if published_before is not None:
            payload['published_before'] = date_to_string(published_before)
            
        if published_after is not None:
            payload['published_after'] = date_to_string(published_after)
            
        if published_on is not None:
            payload['published_on'] = date_to_string(published_on)
        
        # Sort    
        if sort is not None:
            if isinstance(sort, str):
                if sort in const.SORTS:
                    payload['sort'] = sort
                else:
                    raise ValueError('Sort is not valid')
            else:
                raise ValueError('Payload sort must be string')
        
        # Limit        
        if limit is not None:
            if isinstance(limit, int):
                payload['limit'] = limit
            else:
                raise ValueError('Payload language must be integer')
        
        # Page number
        if page is not None:
            if isinstance(page, int):
                if page > 0:
                    payload['page'] = page
                else:
                    raise ValueError('Payload page must be more than 0')
            else:
                raise ValueError('Payload page must be integer')
        
        # Set language if none
        if payload.get("language") is None:
            if isinstance(locale, str):
                payload["language"] = const.DEFAULT_LANGUAGES.get(locale)

        # Get content
        r = requests.get(f'{const.TOP_URL}?api_token={self.api_token}', params=payload)
        
        if not r.ok:
            raise TheNewsAPIException(r.json()['error']['message'])
        
        return r.json()
        
    def get_all_news(self,
        search=None,
        search_fields=None,
        locale=None,
        categories=None,
        exclude_categories=None,
        domains=None,
        exclude_domains=None,
        source_ids=None,
        exclude_source_ids=None,
        language=None,
        published_before=None,
        published_after=None,
        published_on=None,
        sort=None,
        limit=None,
        page=None
    ):
        # Payload
        payload = {}
        
        # Search and search fields
        if search is not None:
            if isinstance(search, str):
                payload['search'] = search
            else:
                raise ValueError('Payload search must be string')
        
        if search_fields is not None:
            for _ in search_fields:
                if _ not in const.FIELDS:
                    raise ValueError('Field is not valid')
            
            if isinstance(search_fields, list):
                payload['search_fields'] = ','.join(search_fields)
            elif isinstance(search_fields, str):
                payload['search_fields'] = search_fields
            else:
                raise ValueError('Payload search_fields must be list')
                
        # Locales
        if locale is not None:
            for _ in locale:
                if _ not in const.LOCALES:
                    raise ValueError('Locale is not valid')
                
            if isinstance(locale, list):
                payload['locale'] = ','.join(locale)
            elif isinstance(locale, str):
                payload['locale'] = locale
            else:
                raise ValueError('Payload locale must be list')
                
        # Categories        
        if categories is not None:
            if isinstance(categories, list):
                for _ in categories:
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['categories'] = ','.join(categories)
            elif isinstance(categories, str):
                for _ in categories.split(','):
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['categories'] = categories
            else:
                raise ValueError('Payload categories must be list')
        
        if exclude_categories is not None:
            if isinstance(exclude_categories, list):
                for _ in exclude_categories:
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['exclude_categories'] = ','.join(exclude_categories)
            elif isinstance(exclude_categories, str):
                for _ in exclude_categories.split(','):
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['exclude_categories'] = exclude_categories
            else:
                raise ValueError('Payload exclude_categories must be list')
        
        # Domains
        if domains is not None:
            if isinstance(domains, list):
                payload['domains'] = ','.join(domains)
            elif isinstance(domains, str):
                payload['domains'] = domains
            else:
                raise ValueError('Payload domains must be list')
                
        if exclude_domains is not None:
            if isinstance(exclude_domains, list):
                payload['exclude_domains'] = ','.join(exclude_domains)
            elif isinstance(exclude_domains, str):
                payload['exclude_domains'] = exclude_domains
            else:
                raise ValueError('Payload exclude_domains must be list')
               
        # Source IDs        
        if source_ids is not None:
            if isinstance(source_ids, list):
                payload['source_ids'] = ','.join(source_ids)
            elif isinstance(source_ids, str):
                payload['source_ids'] = source_ids
            else:
                raise ValueError('Payload source_ids must be list')
                
        if exclude_source_ids is not None:
            if isinstance(exclude_source_ids, list):
                payload['exclude_source_ids'] = ','.join(exclude_source_ids)
            elif isinstance(exclude_source_ids, str):
                payload['exclude_source_ids'] = exclude_source_ids
            else:
                raise ValueError('Payload exclude_source_ids must be list')
        
        # Languages
        if language is not None:
            if isinstance(language, list):
                for _ in language:
                    if _ not in const.LANGUAGES:
                        raise ValueError('Category is not valid')
                payload['language'] = ','.join(language)
            elif isinstance(language, str):
                for _ in language.split(','):
                    if _ not in const.LANGUAGES:
                        raise ValueError('Category is not valid')
                payload['language'] = language
            else:
                raise ValueError('Payload language must be list')
        
        # Published methods | NOTE : Only YYYY-MM-DD and YYYY-MM-DDTHH:MM:SS supported right now
        if published_before is not None:
            payload['published_before'] = date_to_string(published_before)
            
        if published_after is not None:
            payload['published_after'] = date_to_string(published_after)
            
        if published_on is not None:
            payload['published_on'] = date_to_string(published_on)
        
        # Sort    
        if sort is not None:
            if isinstance(sort, str):
                if sort in const.SORTS:
                    payload['sort'] = sort
                else:
                    raise ValueError('Sort is not valid')
            else:
                raise ValueError('Payload sort must be string')
        
        # Limit        
        if limit is not None:
            if isinstance(limit, int):
                payload['limit'] = limit
            else:
                raise ValueError('Payload language must be integer')
        
        # Page number
        if page is not None:
            if isinstance(page, int):
                if page > 0:
                    payload['page'] = page
                else:
                    raise ValueError('Payload page must be more than 0')
            else:
                raise ValueError('Payload page must be integer')
        
        # Set language if none
        if payload.get("language") is None:
            if isinstance(locale, str):
                payload["language"] = const.DEFAULT_LANGUAGES.get(locale)
        
        # Get content
        r = requests.get(f'{const.ALL_URL}?api_token={self.api_token}', params=payload)
        
        if not r.ok:
            raise TheNewsAPIException(r.json()['error']['message'])
        
        return r.json()
    
    def get_similar_news(self,
        uuid,
        categories=None,
        exclude_categories=None,
        domains=None,
        exclude_domains=None,
        source_ids=None,
        exclude_source_ids=None,
        language=None,
        published_before=None,
        published_after=None,
        published_on=None,
        sort=None,
        limit=None,
        page=None
    ):
        # Payload
        payload = {}
                
        # Categories        
        if categories is not None:
            if isinstance(categories, list):
                for _ in categories:
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['categories'] = ','.join(categories)
            elif isinstance(categories, str):
                for _ in categories.split(','):
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['categories'] = categories
            else:
                raise ValueError('Payload categories must be list')
        
        if exclude_categories is not None:
            if isinstance(exclude_categories, list):
                for _ in exclude_categories:
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['exclude_categories'] = ','.join(exclude_categories)
            elif isinstance(exclude_categories, str):
                for _ in exclude_categories.split(','):
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['exclude_categories'] = exclude_categories
            else:
                raise ValueError('Payload exclude_categories must be list')
        
        # Domains
        if domains is not None:
            if isinstance(domains, list):
                payload['domains'] = ','.join(domains)
            elif isinstance(domains, str):
                payload['domains'] = domains
            else:
                raise ValueError('Payload domains must be list')
                
        if exclude_domains is not None:
            if isinstance(exclude_domains, list):
                payload['exclude_domains'] = ','.join(exclude_domains)
            elif isinstance(exclude_domains, str):
                payload['exclude_domains'] = exclude_domains
            else:
                raise ValueError('Payload exclude_domains must be list')
               
        # Source IDs        
        if source_ids is not None:
            if isinstance(source_ids, list):
                payload['source_ids'] = ','.join(source_ids)
            elif isinstance(source_ids, str):
                payload['source_ids'] = source_ids
            else:
                raise ValueError('Payload source_ids must be list')
                
        if exclude_source_ids is not None:
            if isinstance(exclude_source_ids, list):
                payload['exclude_source_ids'] = ','.join(exclude_source_ids)
            elif isinstance(exclude_source_ids, str):
                payload['exclude_source_ids'] = exclude_source_ids
            else:
                raise ValueError('Payload exclude_source_ids must be list')
        
        # Languages
        if language is not None:
            if isinstance(language, list):
                for _ in language:
                    if _ not in const.LANGUAGES:
                        raise ValueError('Category is not valid')
                payload['language'] = ','.join(language)
            elif isinstance(language, str):
                for _ in language.split(','):
                    if _ not in const.LANGUAGES:
                        raise ValueError('Category is not valid')
                payload['language'] = language
            else:
                raise ValueError('Payload language must be list')
        
        # Published methods | NOTE : Only YYYY-MM-DD and YYYY-MM-DDTHH:MM:SS supported right now
        if published_before is not None:
            payload['published_before'] = date_to_string(published_before)
            
        if published_after is not None:
            payload['published_after'] = date_to_string(published_after)
            
        if published_on is not None:
            payload['published_on'] = date_to_string(published_on)
        
        # Sort    
        if sort is not None:
            if isinstance(sort, str):
                if sort in const.SORTS:
                    payload['sort'] = sort
                else:
                    raise ValueError('Sort is not valid')
            else:
                raise ValueError('Payload sort must be string')
        
        # Limit        
        if limit is not None:
            if isinstance(limit, int):
                payload['limit'] = limit
            else:
                raise ValueError('Payload language must be integer')
        
        # Page number
        if page is not None:
            if isinstance(page, int):
                if page > 0:
                    payload['page'] = page
                else:
                    raise ValueError('Payload page must be more than 0')
            else:
                raise ValueError('Payload page must be integer')
        
        # Get content
        r = requests.get(f'{const.SIMILAR_URL}{uuid}?api_token={self.api_token}', params=payload)
        
        if not r.ok:
            raise TheNewsAPIException(r.json()['error']['message'])
        
        return r.json()
        
    def get_news_by_uuid(self,
        uuid
    ):
        # Payload
        payload = {}
        
        # Get content
        r = requests.get(f'{const.BY_UUID_URL}{uuid}?api_token={self.api_token}', params=payload)
        
        if not r.ok:
            raise TheNewsAPIException(r.json()['error']['message'])
        
        return r.json()
        
    def get_sources(self,
        categories=None,
        exclude_categories=None,
        language=None,
        page=None
    ):
        # Payload
        payload = {}
                
        # Categories        
        if categories is not None:
            if isinstance(categories, list):
                for _ in categories:
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['categories'] = ','.join(categories)
            elif isinstance(categories, str):
                for _ in categories.split(','):
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['categories'] = categories
            else:
                raise ValueError('Payload categories must be list')
        
        if exclude_categories is not None:
            if isinstance(exclude_categories, list):
                for _ in exclude_categories:
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['exclude_categories'] = ','.join(exclude_categories)
            elif isinstance(exclude_categories, str):
                for _ in exclude_categories.split(','):
                    if _ not in const.CATEGORIES:
                        raise ValueError('Category is not valid')
                payload['exclude_categories'] = exclude_categories
            else:
                raise ValueError('Payload exclude_categories must be list')
        
        # Languages
        if language is not None:
            if isinstance(language, list):
                for _ in language:
                    if _ not in const.LANGUAGES:
                        raise ValueError('Category is not valid')
                payload['language'] = ','.join(language)
            elif isinstance(language, str):
                for _ in language.split(','):
                    if _ not in const.LANGUAGES:
                        raise ValueError('Category is not valid')
                payload['language'] = language
            else:
                raise ValueError('Payload language must be list')
        
        # Page number
        if page is not None:
            if isinstance(page, int):
                if page > 0:
                    payload['page'] = page
                else:
                    raise ValueError('Payload page must be more than 0')
            else:
                raise ValueError('Payload page must be integer')
        
        # Get content
        r = requests.get(f'{const.SOURCES_URL}?api_token={self.api_token}', params=payload)
        
        if not r.ok:
            raise TheNewsAPIException(r.json()['error']['message'])
        
        return r.json()
    
    def get_headlines(self,
        locale=None,
        domains=None,
        exclude_domains=None,
        source_ids=None,
        exclude_source_ids=None,
        language=None,
        published_on=None,
        sort=None,
        headlines_per_category=None,
        include_similar=None
    ):
        # NOTE : You must be at least standard tier in your thenewsapi.com subscription to use this feature. 
        
        # Payload
        payload = {}
        
                
        # Locales
        if locale is not None:
            for _ in locale:
                if _ not in const.LOCALES:
                    raise ValueError('Locale is not valid')
                
            if isinstance(locale, list):
                payload['locale'] = ','.join(locale)
            elif isinstance(locale, str):
                payload['locale'] = locale
            else:
                raise ValueError('Payload locale must be list')
        
        # Domains
        if domains is not None:
            if isinstance(domains, list):
                payload['domains'] = ','.join(domains)
            elif isinstance(domains, str):
                payload['domains'] = domains
            else:
                raise ValueError('Payload domains must be list')
                
        if exclude_domains is not None:
            if isinstance(exclude_domains, list):
                payload['exclude_domains'] = ','.join(exclude_domains)
            elif isinstance(exclude_domains, str):
                payload['exclude_domains'] = exclude_domains
            else:
                raise ValueError('Payload exclude_domains must be list')
               
        # Source IDs        
        if source_ids is not None:
            if isinstance(source_ids, list):
                payload['source_ids'] = ','.join(source_ids)
            elif isinstance(source_ids, str):
                payload['source_ids'] = source_ids
            else:
                raise ValueError('Payload source_ids must be list')
                
        if exclude_source_ids is not None:
            if isinstance(exclude_source_ids, list):
                payload['exclude_source_ids'] = ','.join(exclude_source_ids)
            elif isinstance(exclude_source_ids, str):
                payload['exclude_source_ids'] = exclude_source_ids
            else:
                raise ValueError('Payload exclude_source_ids must be list')
        
        # Languages
        if language is not None:
            if isinstance(language, list):
                for _ in language:
                    if _ not in const.LANGUAGES:
                        raise ValueError('Category is not valid')
                payload['language'] = ','.join(language)
            elif isinstance(language, str):
                for _ in language.split(','):
                    if _ not in const.LANGUAGES:
                        raise ValueError('Category is not valid')
                payload['language'] = language
            else:
                raise ValueError('Payload language must be list')
        
        # Published methods | NOTE : Only YYYY-MM-DD and YYYY-MM-DDTHH:MM:SS supported right now
        if published_on is not None:
            payload['published_on'] = date_to_string(published_on)
        
        # Headlines per category
        if headlines_per_category is not None:
            if isinstance(headlines_per_category, int):
                payload['headlines_per_category'] = headlines_per_category
            else:
                raise ValueError('Payload headlines_per_category must be integer')
        
        # Include similar        
        if include_similar is not None:
            if isinstance(include_similar, bool):
                    payload['include_similar'] = include_similar
            else:
                raise ValueError('Payload include_similar must be integer')
        
        # Set language if none
        if payload.get("language") is None:
            if isinstance(locale, str):
                payload["language"] = const.DEFAULT_LANGUAGES.get(locale)
        
        # Get content
        r = requests.get(f'{const.HEADLINES_URL}?api_token={self.api_token}', params=payload)
        
        if not r.ok:
            raise TheNewsAPIException(r.json()['error']['message'])
        
        return r.json()
