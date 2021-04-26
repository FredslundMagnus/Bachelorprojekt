
# Parameters

    Name :                      Causal4_Cf_convert2_TopN3-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      65712726252 function calls (65428365405 primitive calls) in 86123.15 seconds

##    Ordered by: cumulative time
   List reduced from 515 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86123.146 86123.146 {built-in method builtins.exec}
                      1    4.876    4.876 86123.146 86123.146 <string>:1(<module>)
                      1  405.845  405.845 86118.270 86118.270 main.py:79(CFagent)
                9026961   44.989    0.000 24251.502    0.003 agent.py:29(learn)
                3008987   16.468    0.000 21170.822    0.007 game.py:41(step)
                3008987   21.351    0.000 20384.870    0.007 layers.py:718(step)
                9026953  630.796    0.000 19511.354    0.002 learner.py:42(Qlearn)
                3008987  301.383    0.000 13084.962    0.004 layers.py:17(step)
              300859730  916.467    0.000 12755.594    0.000 layer.py:98(move)
        318085701/33726545 1410.429    0.000 11246.804    0.000 module.py:866(_call_impl)
               24699592   74.800    0.000 10449.285    0.000 network.py:27(forward)
                3008987  988.172    0.000 10412.707    0.003 agent.py:210(counterfact)
               24699592  351.874    0.000 10192.048    0.000 container.py:117(forward)
                3008987  394.441    0.000 9450.754    0.003 agent.py:54(_learn)
                3008987  386.442    0.000 8531.542    0.003 agent.py:202(_learn)
              300859730 1457.186    0.000 7793.486    0.000 layers.py:735(check)
                9026953   98.042    0.000 7426.304    0.001 optimizer.py:84(wrapper)
                3008987 6263.890    0.002 7318.628    0.002 replaybuffer.py:22(sample_data)
                3008988  487.308    0.000 7244.942    0.002 layers.py:684(update)
                9026953   53.966    0.000 7000.566    0.001 grad_mode.py:24(decorate_context)
                9026953  321.067    0.000 6837.520    0.001 adam.py:55(step)
                3008987 5836.693    0.002 6836.025    0.002 replaybuffer.py:67(sample_data)
                3008987  107.198    0.000 6201.869    0.002 agent.py:117(_learn)
                9026953 1420.585    0.000 6187.765    0.001 _functional.py:53(adam)
                7834963  259.513    0.000 5633.981    0.001 agent.py:49(__call__)
                9026953   43.042    0.000 5231.191    0.001 tensor.py:195(backward)
               48479897 5230.032    0.000 5230.032    0.000 {built-in method tensor}
                9026953   47.458    0.000 5186.765    0.001 __init__.py:68(backward)
               41523208   30.308    0.000 5043.939    0.000 game.py:37(board)
                9026953 4925.266    0.001 4925.266    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3008987 2870.812    0.001 4922.497    0.002 replaybuffer.py:28(teleporter_save_data)
               60179750 2820.490    0.000 4782.417    0.000 layer.py:151(update)
                3008987 2492.813    0.001 4608.868    0.002 agent.py:88(interveen)
               49399184  118.266    0.000 3824.502    0.000 conv.py:398(forward)
               49399184   83.092    0.000 3646.989    0.000 conv.py:390(_conv_forward)
               49399184 3563.897    0.000 3563.897    0.000 {built-in method conv2d}
              300859730  589.923    0.000 3400.573    0.000 layers.py:729(isFree)
               68080802  143.734    0.000 2851.661    0.000 linear.py:93(forward)
             2666935444 2336.149    0.000 2810.650    0.000 layer.py:95(isFree)
                1819710   45.529    0.000 2637.350    0.001 agent.py:175(choose_action)
               68080802   57.906    0.000 2629.276    0.000 functional.py:1737(linear)
               68080802 2557.035    0.000 2557.035    0.000 {built-in method torch._C._nn.linear}
                3008987 1631.315    0.001 2510.696    0.001 agent.py:67(modify)
              192021679 1955.125    0.000 1955.125    0.000 {built-in method clone}
               40933780 1665.347    0.000 1665.347    0.000 {built-in method cat}
             6004782607 1162.789    0.000 1634.139    0.000 enum.py:646(__hash__)
               10843950   90.486    0.000 1611.123    0.000 agent.py:59(modify_board)
                3008979   65.381    0.000 1493.022    0.000 agent.py:171(__call__)
               92780394   85.272    0.000 1487.672    0.000 activation.py:713(forward)
              300312131  331.056    0.000 1430.424    0.000 {built-in method builtins.any}
                3595657   51.862    0.000 1411.714    0.000 layers.py:740(restart)
               92780394   78.283    0.000 1402.400    0.000 functional.py:1364(leaky_relu)
                3008987   61.442    0.000 1365.686    0.000 agent.py:112(__call__)
               92780394 1308.187    0.000 1308.187    0.000 {built-in method torch._C._nn.leaky_relu}
                3008987 1000.974    0.000 1275.938    0.000 replaybuffer.py:73(CF_save_data)
              300859730  938.662    0.000 1234.437    0.000 layers.py:77(check)
              300898800  157.488    0.000 1232.831    0.000 {built-in method builtins.all}
              168503112 1205.473    0.000 1205.473    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1128262293 1196.907    0.000 1196.907    0.000 layer.py:146(elements)
              300859730  717.360    0.000 1130.859    0.000 layers.py:286(check)
             1628262981  448.723    0.000 1115.396    0.000 layers.py:690(<genexpr>)
             3270334573  903.452    0.000 1099.368    0.000 layers.py:700(<genexpr>)
                9026953  196.097    0.000 1067.916    0.000 optimizer.py:189(zero_grad)
               10843950 1064.014    0.000 1064.014    0.000 {built-in method torch._C._nn.one_hot}
              168503112 1061.806    0.000 1061.806    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              300859730  634.484    0.000 1042.295    0.000 layers.py:246(check)
                3595657   24.578    0.000  995.714    0.000 level.py:8(__init__)
                3008987   70.954    0.000  789.840    0.000 replaybuffer.py:18(stacker)
                3595657  128.633    0.000  787.824    0.000 levels.py:199(generate)
             7890805949  752.360    0.000  752.360    0.000 layer.py:91(positions)
                3008979   70.756    0.000  747.959    0.000 replaybuffer.py:63(stacker)
              300859730  548.912    0.000  707.657    0.000 layers.py:62(check)
               84251556  701.042    0.000  701.042    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               84251556  616.512    0.000  616.512    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        8032364776/8032364773  545.734    0.000  609.370    0.000 {built-in method builtins.len}
                7834963  209.011    0.000  599.881    0.000 exploration.py:53(softmaxer)
              300898800  395.091    0.000  580.922    0.000 layers.py:113(isDone)
               84251556  580.836    0.000  580.836    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               84251556  576.429    0.000  576.429    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              300859730  377.015    0.000  573.792    0.000 layers.py:273(check)
               13209288  220.345    0.000  567.611    0.000 random.py:315(sample)
              300859730  367.250    0.000  560.873    0.000 layers.py:313(check)
                7191314   64.053    0.000  532.323    0.000 level.py:41(notUsed)
                1819710  443.652    0.000  501.082    0.000 agent.py:186(convert_values)
              589760976  404.000    0.000  500.299    0.000 tensor.py:906(grad)
                3008987  279.673    0.000  479.796    0.000 collector.py:46(collect)
                9026953   20.761    0.000  478.394    0.000 loss.py:527(forward)
             6004816910  471.357    0.000  471.357    0.000 {built-in method builtins.hash}
                9026953   50.736    0.000  457.634    0.000 functional.py:2898(mse_loss)
              300859730  302.652    0.000  440.434    0.000 layers.py:48(check)
              205874608  419.907    0.000  419.907    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               84251556  419.135    0.000  419.135    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               35956570   50.700    0.000  351.574    0.000 layer.py:69(restart)
              300859730  235.782    0.000  338.506    0.000 layers.py:23(check)
              302485257  226.977    0.000  326.310    0.000 layer.py:126(remove)
              505377864  222.016    0.000  311.785    0.000 layer.py:130(add)
             3323291958  288.457    0.000  288.457    0.000 {method 'random' of '_random.Random' objects}
              387177425  186.425    0.000  278.377    0.000 random.py:250(_randbelow_with_getrandbits)
                9026953  273.432    0.000  273.432    0.000 {built-in method torch._C._nn.mse_loss}
                6017976  269.132    0.000  269.132    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551812: <Causal4_Cf_convert2_TopN3_0> in cluster <dcc> Done

Job <Causal4_Cf_convert2_TopN3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:31 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 22 03:11:47 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 03:11:47 2021
Terminated at Fri Apr 23 03:07:35 2021
Results reported at Fri Apr 23 03:07:35 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85905.30 sec.
    Max Memory :                                 8918 MB
    Average Memory :                             6071.73 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7466.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86151 sec.
    Turnaround time :                            172024 sec.

The output (if any) is above this job summary.

