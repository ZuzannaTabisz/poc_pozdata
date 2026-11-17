
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select linia
from "poz_data"."main"."stg_ztm"
where linia is null



  
  
      
    ) dbt_internal_test