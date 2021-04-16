
# Parameters

    Name :                      ReTest14-0
    Main :                      CFagent
    Level :                     Levels.Coconuts
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      70966539170 function calls (70649570719 primitive calls) in 86107.83 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86107.831 86107.831 {built-in method builtins.exec}
                      1    3.985    3.985 86107.831 86107.831 <string>:1(<module>)
                      1  426.635  426.635 86103.846 86103.846 main.py:75(CFagent)
               11877870   48.793    0.000 29636.069    0.002 agent.py:29(learn)
               11874898  749.063    0.000 24058.203    0.002 learner.py:42(Qlearn)
                3959290   17.084    0.000 23264.109    0.006 game.py:41(step)
                3959290   22.188    0.000 22453.420    0.006 layers.py:718(step)
                3959290  383.413    0.000 15829.030    0.004 layers.py:17(step)
              395683007 1575.469    0.000 15409.027    0.000 layer.py:98(move)
        356575318/39608558 1504.130    0.000 12088.998    0.000 module.py:866(_call_impl)
                3959290  433.881    0.000 11522.401    0.003 agent.py:54(_learn)
               27733660   79.690    0.000 11233.795    0.000 network.py:24(forward)
               27733660  356.208    0.000 10967.844    0.000 container.py:117(forward)
                3959290  428.038    0.000 10577.110    0.003 agent.py:202(_learn)
              395683007 1518.206    0.000 9524.126    0.000 layers.py:735(check)
               11874898  103.165    0.000 9331.570    0.001 optimizer.py:84(wrapper)
               11874898   51.387    0.000 8884.650    0.001 grad_mode.py:24(decorate_context)
               11874898  374.041    0.000 8718.244    0.001 adam.py:55(step)
               11874898 1834.565    0.000 7919.184    0.001 _functional.py:53(adam)
                3959290  123.424    0.000 7460.313    0.002 agent.py:117(_learn)
                3959291  587.288    0.000 6566.826    0.002 layers.py:684(update)
               11874898   47.379    0.000 6258.817    0.001 tensor.py:195(backward)
                3959290 4955.392    0.001 6218.986    0.002 replaybuffer.py:22(sample_data)
               11874898   47.127    0.000 6209.600    0.001 __init__.py:68(backward)
               11874898 5928.057    0.000 5928.057    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3959290 4346.975    0.001 5560.169    0.001 replaybuffer.py:52(sample_data)
                3959290  572.182    0.000 5285.481    0.001 agent.py:210(counterfact)
                7910850  212.753    0.000 5281.418    0.001 agent.py:49(__call__)
                3959290 1979.454    0.000 4578.514    0.001 agent.py:88(interveen)
               55467320  129.207    0.000 4052.344    0.000 conv.py:398(forward)
               55430067 2275.464    0.000 3869.967    0.000 layer.py:151(update)
               55467320   84.568    0.000 3861.512    0.000 conv.py:390(_conv_forward)
                3959290 2171.218    0.001 3826.119    0.001 replaybuffer.py:28(teleporter_save_data)
               55467320 3776.943    0.000 3776.943    0.000 {built-in method conv2d}
               47948263 3713.740    0.000 3713.740    0.000 {built-in method tensor}
               38896314   24.013    0.000 3483.358    0.000 game.py:37(board)
              395683007  621.277    0.000 3241.363    0.000 layers.py:729(isFree)
               75282400  160.823    0.000 3086.585    0.000 linear.py:93(forward)
              395683007 2151.406    0.000 3001.589    0.000 layers.py:471(check)
                3959290 1900.762    0.000 2906.830    0.001 agent.py:67(modify)
               75282400   66.118    0.000 2844.987    0.000 functional.py:1737(linear)
               75282400 2763.565    0.000 2763.565    0.000 {built-in method torch._C._nn.linear}
              395683007 1941.753    0.000 2631.691    0.000 layers.py:77(check)
             2491871093 2225.109    0.000 2620.086    0.000 layer.py:95(isFree)
               51448180 2004.051    0.000 2004.051    0.000 {built-in method cat}
                3956318   71.112    0.000 1828.352    0.000 agent.py:171(__call__)
             6525680104 1232.387    0.000 1757.935    0.000 enum.py:646(__hash__)
                3959290   68.085    0.000 1743.955    0.000 agent.py:112(__call__)
              103016060   83.928    0.000 1634.982    0.000 activation.py:713(forward)
              160383725 1596.197    0.000 1596.197    0.000 {built-in method clone}
               11870140   81.403    0.000 1578.857    0.000 agent.py:59(modify_board)
              103016060   94.591    0.000 1551.054    0.000 functional.py:1364(leaky_relu)
              221660800 1535.596    0.000 1535.596    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1613384   21.333    0.000 1476.253    0.001 layers.py:740(restart)
              103016060 1438.384    0.000 1438.384    0.000 {built-in method torch._C._nn.leaky_relu}
              398275007  329.617    0.000 1388.955    0.000 {built-in method builtins.any}
               11874898  246.223    0.000 1371.796    0.000 optimizer.py:189(zero_grad)
              221660800 1369.431    0.000 1369.431    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1613384    9.653    0.000 1281.870    0.001 level.py:8(__init__)
                3959290  954.649    0.000 1196.984    0.000 replaybuffer.py:58(CF_save_data)
                1613384   79.169    0.000 1188.840    0.001 levels.py:262(generate)
             3154525728  873.656    0.000 1059.338    0.000 layers.py:700(<genexpr>)
               18355661  176.000    0.000 1038.734    0.000 level.py:41(notUsed)
               11870140 1031.059    0.000 1031.059    0.000 {built-in method torch._C._nn.one_hot}
              395683007  780.629    0.000 1015.623    0.000 layers.py:62(check)
                3959290   69.319    0.000  961.115    0.000 replaybuffer.py:18(stacker)
                3956318   64.103    0.000  919.717    0.000 replaybuffer.py:48(stacker)
              110830400  899.596    0.000  899.596    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1094273313  896.922    0.000  896.922    0.000 layer.py:146(elements)
             8490021884  824.612    0.000  824.612    0.000 layer.py:91(positions)
              110830400  799.073    0.000  799.073    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              395929100  152.906    0.000  797.738    0.000 {built-in method builtins.all}
              110830400  725.310    0.000  725.310    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              110830400  725.308    0.000  725.308    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1614735864  435.757    0.000  695.986    0.000 layers.py:690(<genexpr>)
              775812884  529.627    0.000  661.199    0.000 tensor.py:906(grad)
        7907540401/7907540398  564.538    0.000  640.132    0.000 {built-in method builtins.len}
                3959290  362.467    0.000  616.515    0.000 collector.py:46(collect)
              395683007  404.290    0.000  592.646    0.000 layers.py:48(check)
                7918580  217.211    0.000  581.258    0.000 random.py:315(sample)
                7910850  196.890    0.000  536.214    0.000 exploration.py:53(softmaxer)
              110830400  535.695    0.000  535.695    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             6525725047  525.558    0.000  525.558    0.000 {built-in method builtins.hash}
               11874898   16.069    0.000  525.413    0.000 loss.py:527(forward)
               11874898   46.314    0.000  509.344    0.000 functional.py:2898(mse_loss)
                3959290   90.276    0.000  509.182    0.000 agent.py:277(counterfact_check)
               18355661   19.925    0.000  462.401    0.000 level.py:38(elementsIn)
              395683007  308.594    0.000  448.043    0.000 layers.py:23(check)
              402276898  264.526    0.000  394.603    0.000 layer.py:126(remove)
              176210183  379.985    0.000  379.985    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               11874898  311.809    0.000  311.809    0.000 {built-in method torch._C._nn.mse_loss}
               27715030  308.701    0.000  308.701    0.000 {built-in method sum}
              492053432  219.795    0.000  299.309    0.000 layer.py:130(add)
               18355661  143.622    0.000  291.677    0.000 level.py:39(<listcomp>)
               11876084  282.666    0.000  282.666    0.000 {built-in method max}
                7918582  277.150    0.000  277.150    0.000 {built-in method nonzero}
             3173628629  276.674    0.000  276.674    0.000 {method 'random' of '_random.Random' objects}
               55467320   40.699    0.000  275.848    0.000 flatten.py:39(forward)
             2491871093  265.682    0.000  265.682    0.000 layer.py:203(isBlocking)
              415090776  180.588    0.000  265.432    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-16>
Subject: Job 9515521: <ReTest14_0> in cluster <dcc> Done

Job <ReTest14_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 14 15:03:58 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 14 16:05:05 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 14 16:05:05 2021
Terminated at Thu Apr 15 16:00:20 2021
Results reported at Thu Apr 15 16:00:20 2021

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

    CPU time :                                   85895.75 sec.
    Max Memory :                                 11001 MB
    Average Memory :                             7049.80 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5383.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            89782 sec.

The output (if any) is above this job summary.

