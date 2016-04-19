calculate_field = function(y_center, radius, output_name)
	y_arcstart = y_center-radius
	y_arcend = y_center+radius
	
	window_width = 600

	newdocument(1)	
	
	-- Dynamic inside circle
	ei_addnode(0, y_arcstart)
	ei_addnode(0, y_arcend)
	ei_addarc(0, y_arcstart, 0, y_arcend, 180, 1)
	
	-- Static enclosing circle
	ei_addnode(0, 2)
	ei_addnode(0, -2)
	ei_addarc(0, -2, 0, 2, 180, 1)
	
	-- Segments on symmetry axis connecting arcs
	ei_addsegment(0, y_arcstart, 0, -2)
	ei_addsegment(0, y_arcend, 0, 2)
	
	-- Create and assign material
	ei_addmaterial("air", 1, 1, 0)
	ei_addblocklabel(1.999999, 0)
	ei_selectlabel(1.999999, 0)
	ei_setblockprop("air", 1, 0, 0)
	ei_clearselected()
	
	-- Create and assign conductor boundary conditions
	ei_addconductorprop("hv", 1, 0, 1)
	ei_addconductorprop("gnd", 0, 0, 1)
	
	ei_selectarcsegment(2,0)
	ei_setarcsegmentprop(1, "", 0, 0, "gnd")
	ei_clearselected()
	
	ei_selectarcsegment(0, y_arcstart)
	ei_setarcsegmentprop(1, "", 0, 0, "hv")
	ei_clearselected()
	
	ei_resize(window_width, window_width)
	ei_zoomnatural()
	
	-- Define problem, save geometry, solve
	ei_probdef("centimeters", "axi", 1e-008, 1, 30)
	ei_saveas("test.FEE")
	ei_analyze()
	ei_loadsolution()
	
	-- Show density plot, rescale, zoom to fit, capture bitmap
	eo_showdensityplot(0, 0, 2, 300, 0)
	eo_resize(window_width, window_width)
	eo_zoomnatural()
	eo_savebitmap(output_name .. ".bmp")
	
	-- Extract results
	r = abs(y_arcend-y_arcstart)/2
	y_center = y_arcstart + r
	
	f = openfile(output_name .. ".dat", "w+")
	for i = 1, 179 do
		-- Compute locations of probing points
		x_p = r * sin(rad(i))
		y_p = -r * cos(rad(i)) + y_center
			
		-- Scale so we always probe slightly outside the inner circle
		V,Dx,Dy,Ex,Ey,ex,ey,nrg = eo_getpointvalues(x_p*1.01, y_p*1.01)
	
		-- For some reason results are not always available
		if Ex == nil then
			write(f, -1, "\n")	
		else
			E_m = sqrt(Ex*Ex + Ey*Ey)
			write(f, E_m, "\n")
		end
	end
	closefile(f)	
end