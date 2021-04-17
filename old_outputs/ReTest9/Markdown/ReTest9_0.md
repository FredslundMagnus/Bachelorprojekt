
# Parameters

    Name :                      ReTest9-0
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      75450147257 function calls (75173813102 primitive calls) in 86114.24 seconds

##    Ordered by: cumulative time
   List reduced from 503 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.235 86114.235 {built-in method builtins.exec}
                      1    4.118    4.118 86114.235 86114.235 <string>:1(<module>)
                      1  344.272  344.272 86110.117 86110.117 main.py:75(CFagent)
               10298301   38.317    0.000 28641.481    0.003 agent.py:29(learn)
               10297666  660.822    0.000 23682.508    0.002 learner.py:42(Qlearn)
                3432767   14.052    0.000 20345.088    0.006 game.py:41(step)
                3432767   20.494    0.000 19533.956    0.006 layers.py:718(step)
                3432767  295.342    0.000 13261.487    0.004 layers.py:17(step)
              342715470  956.693    0.000 12935.784    0.000 layer.py:98(move)
                3432767  114.014    0.000 11085.504    0.003 agent.py:54(_learn)
        310802091/34469627 1131.578    0.000 11016.963    0.000 module.py:715(_call_impl)
               24171961   55.199    0.000 10288.888    0.000 network.py:24(forward)
                3432767  112.233    0.000 10267.896    0.003 agent.py:202(_learn)
               24171961  281.356    0.000 10087.838    0.000 container.py:115(forward)
               10297666   60.756    0.000 9639.330    0.001 grad_mode.py:23(decorate_context)
               10297666  335.489    0.000 9470.527    0.001 adam.py:55(step)
                3432767 1471.022    0.000 8866.135    0.003 agent.py:210(counterfact)
              342715470 1526.061    0.000 7832.157    0.000 layers.py:735(check)
               10297666 1738.786    0.000 7783.558    0.001 functional.py:53(adam)
                3432767   93.811    0.000 7229.538    0.002 agent.py:117(_learn)
                3432768  483.812    0.000 6222.042    0.002 layers.py:684(update)
                3432767 4521.145    0.001 5979.185    0.002 replaybuffer.py:22(sample_data)
               57122690 5889.459    0.000 5889.459    0.000 {built-in method tensor}
               49231289   27.306    0.000 5682.743    0.000 game.py:37(board)
                3432767 4067.969    0.001 5505.113    0.002 replaybuffer.py:52(sample_data)
               10297666   58.395    0.000 5491.263    0.001 tensor.py:181(backward)
               10297666   33.192    0.000 5432.868    0.001 __init__.py:68(backward)
               10297666 5178.172    0.001 5178.172    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                6929811  155.478    0.000 4803.111    0.001 agent.py:49(__call__)
                3432767 2000.280    0.001 4377.923    0.001 agent.py:88(interveen)
               68655350 2486.286    0.000 4286.462    0.000 layer.py:151(update)
                3432767 2081.995    0.001 3849.793    0.001 replaybuffer.py:28(teleporter_save_data)
               48343922   77.745    0.000 3668.478    0.000 conv.py:422(forward)
               48343922   88.157    0.000 3554.778    0.000 conv.py:414(_conv_forward)
              342715470  647.095    0.000 3505.007    0.000 layers.py:729(isFree)
               48343922 3447.591    0.000 3447.591    0.000 {built-in method conv2d}
               65650349  138.410    0.000 3285.310    0.000 linear.py:92(forward)
               65650349  246.572    0.000 3073.751    0.000 functional.py:1669(linear)
                3432767 1524.131    0.000 2997.005    0.001 agent.py:67(modify)
             3317306351 2358.087    0.000 2857.912    0.000 layer.py:95(isFree)
               44687073 2554.026    0.000 2554.026    0.000 {built-in method cat}
              672777966 1448.052    0.000 2413.241    0.000 tensor.py:933(grad)
             1299330429  671.745    0.000 2360.341    0.000 {built-in method builtins.any}
                3432767 1472.234    0.000 2215.253    0.001 replaybuffer.py:58(CF_save_data)
               65650349 2145.480    0.000 2145.480    0.000 {built-in method addmm}
               10297666  193.412    0.000 2082.404    0.000 optimizer.py:167(zero_grad)
              176481489 1847.740    0.000 1847.740    0.000 {built-in method clone}
                3432132   51.270    0.000 1649.790    0.000 agent.py:171(__call__)
              192222252 1582.512    0.000 1582.512    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3432767   51.829    0.000 1537.003    0.000 agent.py:112(__call__)
             6362826427 1059.742    0.000 1515.109    0.000 enum.py:646(__hash__)
               10362578   63.652    0.000 1438.775    0.000 agent.py:59(modify_board)
               89822310   70.594    0.000 1410.751    0.000 activation.py:713(forward)
               89822310  119.794    0.000 1340.157    0.000 functional.py:1292(leaky_relu)
              192222252 1306.795    0.000 1306.795    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              869027464  432.734    0.000 1299.666    0.000 overrides.py:1070(has_torch_function)
              342715470  983.654    0.000 1282.779    0.000 layers.py:77(check)
               34488575  174.101    0.000 1263.694    0.000 tensor.py:21(wrapped)
                3432767   57.174    0.000 1220.756    0.000 replaybuffer.py:18(stacker)
               89822310 1209.969    0.000 1209.969    0.000 {built-in method torch._C._nn.leaky_relu}
                3432132   55.988    0.000 1204.494    0.000 replaybuffer.py:48(stacker)
             3746869676  992.337    0.000 1198.018    0.000 layers.py:700(<genexpr>)
              342715470  704.351    0.000 1088.118    0.000 layers.py:246(check)
              342715470  619.448    0.000 1012.541    0.000 layers.py:286(check)
             1061645049 1004.573    0.000 1004.573    0.000 layer.py:146(elements)
                2652284   32.656    0.000  954.806    0.000 layers.py:740(restart)
               10362578  930.571    0.000  930.571    0.000 {built-in method torch._C._nn.one_hot}
              377765375  156.530    0.000  920.231    0.000 {built-in method builtins.all}
               96111126  896.523    0.000  896.523    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               96111126  845.804    0.000  845.804    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1584885802  424.768    0.000  780.482    0.000 layers.py:690(<genexpr>)
             8525323293  760.435    0.000  760.435    0.000 layer.py:91(positions)
               96111126  739.605    0.000  739.605    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              342715470  556.145    0.000  706.785    0.000 layers.py:62(check)
                2652284   15.166    0.000  676.489    0.000 level.py:8(__init__)
               96111126  646.246    0.000  646.246    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        8279007591/8279007588  493.891    0.000  609.565    0.000 {built-in method builtins.len}
                3432767  349.328    0.000  597.112    0.000 collector.py:46(collect)
              342715470  374.529    0.000  570.809    0.000 layers.py:313(check)
              190276199  541.843    0.000  541.843    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2652284   94.317    0.000  535.913    0.000 levels.py:199(generate)
              342715470  330.992    0.000  518.702    0.000 layers.py:273(check)
                6929811  180.571    0.000  500.681    0.000 exploration.py:53(softmaxer)
               12170102  188.953    0.000  498.657    0.000 random.py:315(sample)
             1838193160  391.702    0.000  484.201    0.000 overrides.py:1083(<genexpr>)
               10297666   13.254    0.000  482.911    0.000 loss.py:445(forward)
               96111126  482.095    0.000  482.095    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10297666   53.289    0.000  469.657    0.000 functional.py:2637(mse_loss)
                3432767   81.456    0.000  461.505    0.000 agent.py:277(counterfact_check)
             6362865546  455.374    0.000  455.374    0.000 {built-in method builtins.hash}
              342715470  303.992    0.000  444.871    0.000 layers.py:48(check)
                6866283  434.439    0.000  434.439    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               24029369  425.559    0.000  425.559    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               65650349  408.020    0.000  408.020    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5304568   43.046    0.000  360.628    0.000 level.py:41(notUsed)
              342715470  241.274    0.000  357.154    0.000 layers.py:23(check)
              306491634  241.130    0.000  326.868    0.000 layer.py:126(remove)
             3785253786  299.579    0.000  299.579    0.000 {method 'random' of '_random.Random' objects}
               24029369  276.421    0.000  276.421    0.000 {built-in method sum}
               10297666  272.800    0.000  272.800    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9514999: <ReTest9_0> in cluster <dcc> Done

Job <ReTest9_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Wed Apr 14 13:56:06 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 14 14:21:04 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 14 14:21:04 2021
Terminated at Thu Apr 15 14:16:23 2021
Results reported at Thu Apr 15 14:16:23 2021

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

    CPU time :                                   85899.27 sec.
    Max Memory :                                 3306 MB
    Average Memory :                             3283.03 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13078.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86121 sec.
    Turnaround time :                            87617 sec.

The output (if any) is above this job summary.

