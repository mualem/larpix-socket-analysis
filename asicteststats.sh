#/usr/bin/bash
#
#
export datadir='/home/mualem/gh-socket-testing/larpix-socket-analysis/data'
export analysisdir='/home/mualem/gh-socket-testing/larpix-socket-analysis/'
export batch=$1
export netconfigfile=netconfig$batch.csv
export bpsfile=bps-summary$batch.csv
export netsummaryfile=netsummary$batch.csv
export batchsummaryfile=batchsummary$batch.csv
batchdir=$datadir/$batch
if [ ! -d $batchdir ] ; then echo -e "\nBatch Directory $batchdir not found\n" ; exit ; fi
cd $batchdir
echo checking netconfigfile $netconfigfile
eval $(head -2 $netconfigfile | grep -v Test | awk -F ',' '{print "export StartTime="$1 "; export StartSN="$2}' )
eval $(tail -n 1 $netconfigfile | awk -F ',' '{print "export EndTime="$1 ";export EndSN="$2}')
((asics=`awk -F , '{print $2}'  $netconfigfile  | uniq |grep -c ''` - 1 ))
#echo $asics1
#(( asics= $asics1 - 1 ))
#echo $asics

# run netconfig analysis to characterize ASICS good/bad
python ${analysisdir}netconfig_analyze.py $netconfigfile
# run summaryPlots_2025_v3.py to analyze bps/noise data
python ${analysisdir}summaryPlots_2025_v3.py $bpsfile
# run batch_analyze.py to combine results of above in one summary
python ${analysisdir}batch_analyze.py $netsummaryfile

echo -e "\nChecking for swapfiles"
# check for bitswap files and append ,bitswap to th summary SN line
swaplist=(bitswap*)
#echo $swaplist
if [ -f $swaplist ] ; then
	for bitswap in `ls bitswap*` ; do
		# extract SN from name
		#echo $bitswap
		export swapsn=`basename $bitswap .h5 | awk -F '-' '{print $4}'`
		echo $swapsn
		sed -i '/'${swapsn}'/s/$/,bitswap/' ${batchsummaryfile}
	done
else
	echo -e  "No bitswap files found\n"
fi



#pwd
#ls -l batchsummary*
export GoodTests=$(grep -v ChipSN batchsummary* | grep -v bitswap | grep -i -c -h -e GoodBps)
export NoiseFails=$(grep -v ChipSN batchsummary* | grep -i -c -h -e BadBps -e 'Good,,' -e bitswap)
export CommFails=$(grep -v ChipSN batchsummary* | grep -v bitswap | grep -i -c -h -e ',bad,')

echo Noisefails:
grep -v ChipSN batchsummary* | grep -i -h -e BadBps -e 'Good,,'
echo
echo CommFails:
grep -v ChipSN batchsummary* | grep -i -h -e ',bad,'

# print the statistics
echo
echo 'batch  StartSN  EndSN   asics   StartTime    EndTime   GoodTests   NoiseFails  CommFails'
echo -e "${batch} ${StartSN} ${EndSN} ${asics} ${StartTime} ${EndTime} ${GoodTests} ${NoiseFails} ${CommFails}"  
