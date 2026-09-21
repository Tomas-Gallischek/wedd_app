from django.db import models

class xp(models.Model):
    on_xp = models.IntegerField(default=0, verbose_name="XP ON")
    on_lvl = models.IntegerField(default=1, verbose_name="LVL ON")
    on_xp_need = models.IntegerField(default=5, verbose_name="XP potřebné pro další level")
    
    ona_xp = models.IntegerField(default=0, verbose_name="XP ONA")
    ona_lvl = models.IntegerField(default=1, verbose_name="LVL ONA")
    ona_xp_need = models.IntegerField(default=5, verbose_name="XP potřebné pro další level")
    
    def save(self, *args, **kwargs):
        if not self.pk and xp.objects.exists():
            raise ValueError("Může existovat pouze jeden záznam XP.")
        
        if self.on_xp >= self.on_xp_need:
            self.on_lvl += 1
            self.on_xp -= self.on_xp_need
            self.on_xp_need = int(round(self.on_xp_need * 1.5))
            
        if self.ona_xp >= self.ona_xp_need:
            self.ona_lvl += 1
            self.ona_xp -= self.ona_xp_need
            self.ona_xp_need = int(round(self.ona_xp_need * 1.5))
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"XP ON: {self.on_xp}, XP ONA: {self.ona_xp}"